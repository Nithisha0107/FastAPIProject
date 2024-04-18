from pydantic import BaseModel,EmailStr
from typing import Optional

class StudentIn(BaseModel):

    name : str
    age : Optional[int]

class StudentOut(StudentIn):
    id : int 
    
    class Config:
        orm_mode = True
    

class UserIn(BaseModel):
    name :str
    email :EmailStr
    password : str 

class UserOut(BaseModel):
    id : int 
    name :str
    password:str
    # class Config:
    #     orm_mode = True


