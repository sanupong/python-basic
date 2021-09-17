# Route Parameters and String Query

from typing import Optional
from fastapi import FastAPI

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


