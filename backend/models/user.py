from sqlalchemy import column, Integer, String,Float,ForeignKey
from backend.database import Base

class Factory(Base):
    __tablename__="factories"
    id=column(Integer,primary_key=True,index=True)
    name=column(String,unique=True)
    subscription=column(String)

class user(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    email=Column(String)
    password=Column(String)
    subscription=Column(String)

class productionData(Base):
    __tablename__="production_Data"
    id=column(Integer,primary_key=True)
    factory_id=column(Integer)
    quantity=column(Float)

class MachineData(Base):
    __tablename__="machine_data"
    id=column(Integer,primary_key=True)
    factory_id=column(Integer)
    hours_used=column(Float)
    temperature=column(Float)
    failure=column(Integer)
