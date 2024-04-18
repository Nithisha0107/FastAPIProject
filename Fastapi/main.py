from fastapi import FastAPI,status,Response,HTTPException,Depends
from pydantic import BaseModel
from typing import Optional
import  models 
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from schemas import *
import utils

models.Base.metadata.create_all(bind = engine)
app= FastAPI()

#dependency


@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    return {"status":"success"}

class Post(BaseModel):
    title:str
    content:str
    rating:Optional[int] = None

@app.post("/")
def get_data(request:Post):
    return {"data":request}

@app.get("/")
def abc():
    return "Hello World"

@app.post("/student",status_code = status.HTTP_201_CREATED,response_model = StudentOut)
def stu_post(request:StudentIn,db:Session = Depends(get_db),status_code = 201):
    post = models.Student(
      
        **request.dict()
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return {'post':post}


@app.get("/student")
def stu_get(db:Session = Depends(get_db)):
    get = db.query(models.Student).all()
    return get

@app.get('/student/{id}')
def stu_get_unique(id:int,db:Session = Depends(get_db)):
    
    get = db.query(models.Student).filter(models.Student.id == id).first()
    return get

@app.post('/user',status_code = status.HTTP_201_CREATED,response_model = UserOut)
def create_user(req:UserIn,db : Session = Depends(get_db)):
    

    hashed_password = utils.hash(req.password)
    req.password = hashed_password
    post = models.User(**req.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

@app.get('/users/{id}')
def get_user(id = id,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

    return user    