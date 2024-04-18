from database import Base
from sqlalchemy import Column , Integer,String


class Student(Base):
    __tablename__ = "Studentdata"

    id = Column(Integer,primary_key = True,nullable = False)
    name = Column(String,nullable = False)
    age = Column(Integer,nullable = True)

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer,primary_key  =True,nullable = False)
    name = Column(String,nullable = False)
    email = Column(String,unique = True,nullable = False)
    password = Column(String,unique=True,nullable = False)


