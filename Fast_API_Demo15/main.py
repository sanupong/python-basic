# response Model with Exclude Option 
# Before pip3 install email-validator

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

# Don't do this in production!
#@app.post("/user/", response_model=UserOut)
@app.post("/user/", response_model=UserIn, response_model_exclude={"password","email"}) # Exclude Option
async def create_user(user: UserIn):
    return user
