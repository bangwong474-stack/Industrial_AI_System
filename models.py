from sqlalchemy import column, Integer, String,Float,ForeignKey
from database import Base

class Factory(Base):
    __tablename__="factories"
    id=column(Integer,primary_key=True,index=True)
    name=column(String,unique=True)
    subscription=column(String)

class user(Base):
    __tablename__="users"
id=column(Integer,primary_key=True,index=True)
username=column(String,unique=True)
role=column(String)
factory_id=column(Integer,ForeignKey("factories.id"))

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
