# Other PUT DELETE POST and Doc Gen. (Swagger)

from typing import Optional
from fastapi import FastAPI, Form

from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str

app = FastAPI()

@app.get("/") #define route
def get_root():
    return{"root":"yes"}

@app.get("/courses")
def get_courses():
    return ["Angular","VueJS"]

@app.get("/course/{id}")
def get_courses_by_id(id:int):
    return ["Angular","VueJS"][id]

@app.get("/auth/{action}/{token}")
# sampe -> http://127.0.0.1:8000/auth/login/1234?q1=test 
def get_action_and_token(action:str, token:str, q1:Optional[str]=None):
    return {"action":action, "token":token, "q1":q1}

@app.post("/login")
def post_login(user:User):
    return{"login": user}

@app.post("/register")
def post_register(username: str = Form(...), password: str = Form(...)):
    return{"username": username, "password":password}

@app.delete("/user/{id}")
def delete_user(id:int, user:User):
    return{"delete": id, "user":user}


@app.put("/user/{id}")
def update_user(id:int, user:User):
    return{"update": id, "user":user}



