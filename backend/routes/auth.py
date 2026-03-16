from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel
from models.user import User
from sqlalchemy.orm import Session
from database import get_db

router=APIRouter()


class LoginData(BaseModel):
    email:str
    password:str


@router.post("/login")
def login(data:LoginData,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.email==data.email).first()

    if not user:
        return{"message":"user not found"}
    
    return{"message":"user found"}