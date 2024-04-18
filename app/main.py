import models
from schemes import *
from fastapi import FastAPI,status,HTTPException
from database import *
from routers import users,auth



app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

