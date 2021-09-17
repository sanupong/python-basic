# Login and Register อย่างง่ายด้วย PassLib

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# Before code should install pip3 install "passlib[bcrypt]"

from typing import Optional
from fastapi import FastAPI
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # pwd_context is variable to contain function encrypted

app = FastAPI()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


# password = "1234"
# hashed_password = get_password_hash(password)
# print(hashed_password)

# if verify_password(password, hashed_password):
#     print("password is correct")
# else:
#     print("password is incorrect")

users = {}

@app.get("/register")
def register(username:str, password:str):
    users[username] = get_password_hash(password)
    return users

@app.get("/login")
def login(username:str, password:str):
    try:
        hashed_password = users[username]
        #if hashed_password and verify_password(password, hashed_password):
        if verify_password(password, hashed_password):
            return {"login":"ok"}
        else:
            return {"login":"Invalid password"}
    except:
         return {"login":"Invalid username"}




