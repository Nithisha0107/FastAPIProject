import utils
import models
from fastapi import status,FastAPI,HTTPException,APIRouter,Depends
from schemes import * 
from database import * 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/users',
    tags = ['users']
)

@router.post('/',response_model = UserOut,status_code = status.HTTP_201_CREATED)
def create_user(request :UserIn,db:Session = Depends(get_db)):

    hashed_password = utils.hash(request.password)
    request.password = hashed_password

    user = models.User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@router.get('/{id}',response_model = UserOut)
def retrive_user(id = id, db : Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id ==id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
    return user

@router.put('/{id}',response_model = UserOut,status_code = status.HTTP_202_ACCEPTED)
def put_user(id:int,request:UserIn,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    for key, value in request.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.delete('/{id}',response_model = UserOut,status_code = status.HTTP_202_ACCEPTED)
def put_user(id:int,db:Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).delete(synchronize_session = False)
    
    db.commit()
    db.refresh(user)
    return {"response":"User deleted succussfully"}
    


