from schemes import * 
from database import Base 
from sqlalchemy import Column,Integer,String
from sqlalchemy.types import ARRAY




class employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer,primary_key = True,nullable = False)
    name= Column(String,unique = True,nullable  =False)
    phone  = Column(Integer,nullable = False)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer,primary_key = True)
    username = Column(String,nullable = False)
    password = Column(String,nullable = False)
    email = Column(String,nullable = False,unique = True)
    address = Column(ARRAY(String))
