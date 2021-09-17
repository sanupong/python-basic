# POST Json

from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str

# curl totorial
# https://www.youtube.com/wath?v=--LEfrXsx7g

app = FastAPI()

@app.post("/login")
def post_login():
    return{"login":"yes"}

@app.post("/register")
def post_login(user:User):
    return{"register": user}