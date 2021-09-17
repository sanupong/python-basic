# POST Json
# Must install "pip3 install python-multipart" before Because of this demo has binary field such as Form(...) FastAPI Detect need python-multipart

from typing import Optional
from fastapi import FastAPI, Form


# curl totorial
# https://www.youtube.com/wath?v=--LEfrXsx7g

app = FastAPI()

@app.post("/register")
def post_register(username: str = Form(...), password: str = Form(...)):
    return{"username": username, "password":password}

