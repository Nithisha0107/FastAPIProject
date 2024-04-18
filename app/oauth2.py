from jose import jwt,JWTError 
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
import database,models


outh2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')


SECRET_KEY = "HI"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

def create_access_token(data:dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp":expire})
    encoded_jwt = jwt.encode(payload,SECRET_KEY,algorithm = ALGORITHM)
    return encoded_jwt

def decode_token(token:str,credentials_exception):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return {"toten_data": payload}
    except JWTError:
        raise  credentials_exception
    
def get_current_user(token: str = Depends(outh2_scheme),db:Session = Depends(database.get_db)):
    credendials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,details = f"Could not validate credentials",headers = {"WWW-Authenticate":"Bearer"})
    token =  decode_token(token,credendials_exception)  
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user

    

