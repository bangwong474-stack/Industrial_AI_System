from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from models.user import User
from sqlalchemy.orm import Session
from database import get_db

router=APIRouter()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

class LoginData(BaseModel):
    email:str
    password:str


@router.post("/login")
def login(data:LoginData,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.email==data.email).first()

    if not user:
        raise HTTPException(status_code=400,detail="Invalid credentials")
    
    if not pwd_context.verify(data.password,user.password):
        raise HTTPException(status_code=400,detail="Invalid credentials")
    
    return{"message":"Login successfully"}