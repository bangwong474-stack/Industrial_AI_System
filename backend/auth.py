from jose import JWTError,jwt
from datetime import datetime,timedelta
from config import FLUTTERWAVE_SECRET_KEY,API_TOKEN

ALGORITHM="HS256"
FLUTTERWAVE_SECRET_KEY="supersecretkey"

def create_token(data:dict):
    expire=datetime.utcnow()+timedelta(hours=2)
    data.update({"exp":expire})
    return jwt.encode(data,FLUTTERWAVE_SECRET_KEY,algorithm=ALGORITHM)

def authenticate(token):
    if token==f"Bearer{API_TOKEN}":
        return True
    return False