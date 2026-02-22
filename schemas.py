from pydantic import BaseModel

class ProductionRequest(BaseModel):
    month:float

class MachineRequest(BaseModel):
    hours:float
    temperature:float

class UserCreate(BaseModel):
    username:str
    password:str
    role:str
    factory_id:int