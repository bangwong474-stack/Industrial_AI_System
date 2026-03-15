from fastapi import FastAPI,Request,Depends,HTTPException
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
import uvicorn
import numpy as np
from sklearn.linear_model import LinearRegression
from routes.auth import login
from ai_machine import predict
from billing import create_checkout_session
from fastapi import UploadFile,File
import pandas as pd
import io
import os
import joblib
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from routes import payment
from database import Base,engine
from models import user

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(auth.router)
app.include_router(payment.router)


#=====LOAD MODEL======
with open("model.pkl","rb")as file:
    model=joblib.load("model.pkl")

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

    current_user=False

    if not current_user.is_active:
        return{"message":"please subscribe first"}
    
    result=model.predict([list(data.values())])
    return{"prediction":result.tolist()}

@app.post("/chat")
async def chat(data:dict):
    message=data["message"]
    return{"reply":"You said:"+message}


@app.get("/")
def home():
    return{"message":"Hello World! FastAPI app is live"}

@app.get("/about")
def about():
    return{"message":"This is my API"}

@app.post("/verify_payment")
def verify_payment(payment_token:str):
    payment_secret_key=os.environ("PAYMENT_SECRET_KEY")
    if not payment_secret_key:
        raise HTTPException(status_code=400,detail="Secret key missing")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    

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

@app.post("/upload-excel")
async def upload_excel(file:UploadFile=File(...)):
    contents=await file.read()

    df=pd.read_excel(io.BytesIO(contents))

    summary={"rows":len(df),"columns":list(df.columns)}

    return summary

@app.get("/subscribe/{plan}")
def subscribe(plan:str):
    url=create_checkout_session(plan)
    return{"checkout_url":url}