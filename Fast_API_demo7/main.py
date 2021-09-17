# Path Parameters EP1
# https://fastapi.tiangolo.com/tutorial/path-params/

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}") # <-- This's Path parameter
def read_item(item_id:int):
    return {"item_id": item_id}

# Order matters /users/me ควรอยู่ก่อน /users/{dynamic}
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}