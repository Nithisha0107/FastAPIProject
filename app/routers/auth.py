from fastapi import APIRouter, Depends,status,HTTPException,Response
from database import *
from sqlalchemy.orm import Session
from schemes import *
import models,utils,oauth2


router = APIRouter(tags = ['Authentication'])

@router.post('/login',response_model='Token')
def login(user_credentials:UserLogin,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN)
    
    if not utils.verify(user_credentials.password,user.password):
       raise HTTPException(status_code = status.HTTP_403_FORBIDDEN)
    

    return oauth2.create_access_token(data = {"user_id": user.id})

    
    
