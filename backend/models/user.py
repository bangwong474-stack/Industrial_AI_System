from sqlalchemy import Column, Integer, String,Float,ForeignKey
from database import Base

class Factory(Base):
    __tablename__="factories"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    subscription=Column(String)

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    email=Column(String)
    password=Column(String)
    subscription=Column(String)

class ProductionData(Base):
    __tablename__="Production_Data"
    id=Column(Integer,primary_key=True)
    factory_id=Column(Integer)
    quantity=Column(Float)

class MachineData(Base):
    __tablename__="machine_data"
    id=Column(Integer,primary_key=True)
    factory_id=Column(Integer)
    hours_used=Column(Float)
    temperature=Column(Float)
    failure=Column(Integer)
