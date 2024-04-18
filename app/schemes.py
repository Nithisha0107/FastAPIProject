from pydantic import BaseModel,EmailStr
from typing import Optional ,List

class EmployeeIn(BaseModel):
    name :str 
    address : str
    phone  : int 

class EmployeeOut(BaseModel):
    id:int
    name : str 

class UserIn(BaseModel):
    
    username:str
    password : str 
    email :EmailStr 
    address :List[str] 

class UserOut(BaseModel):
    #id :int 
    username:str
    email :EmailStr
    #address :list[str]

class UserLogin(BaseModel):
    username : str
    password:str
