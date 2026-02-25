from fastapi import FastAPI,Request,Depends,HTTPException
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
import uvicorn
import numpy as np
from auth import authenticate
from ai_machine import predict
from billing import create_checkout_session
import os
import pickle


app=FastAPI(docs_url=None,redoc_url=None)

#=====LOAD MODEL======
with open("model.pkl","rb")as file:
    model=pickle.load(file)

print(model)

#=====AUTHENTICATION=====
security=HTTPBearer()

API_KEY=os.getenv("API_KEY")

def verify_token(token:str=Depends(security)):
    if token.credentials!=API_KEY:
        raise HTTPException(status_code=403,tail="Unauthorized")
    
#======END POINT======
@app.post("/predict")
def predict(data:dict,token:str=Depends(verify_token)):
    result=model.predict([list(data.values())])
    return{"prediction":result.tolist()}


@app.get("/")
def home():
    return{"message":"Hello World! FastAPI app is live"}

@app.post("/verify_payment")
def verify_payment(payment_token:str):
    payment_secret_key=os.environ("PAYMENT_SECRET_KEY")
    if not payment_secret_key:
        raise HTTPException(status_code=400,detail="Secret key missing")
    

if __name__=="__main__":
    port=int(os.environ.get("PORT",10000))
    app.get(host="0.0.0.0",port=port)

@app.post("/predict/production")
def production(data:dict,request:Request):
    token=request.headers.get("Authorization")
    if not authenticate(token):
        return{"error":"Unauthorized"},401
    month=data.get("month")
    result=predict(month)
    return{"predicted_production":result}

@app.post("/predict/machine")
def machine(data:dict,request:Request):
    token=request.headers.get("Authorization")
    if not authenticate(token):
        return{"error":"Unauthorized"},401
    hours=data.get("hours")
    temperature=data.get("temperature")
    result=predict(hours,temperature)
    status="FAILURE" if result==1 else "MACHINE OK"
    return{"machine_status":status}

@app.get("/subscribe/{plan}")
def subscribe(plan:str):
    url=create_checkout_session(plan)
    return{"checkout_url":url}