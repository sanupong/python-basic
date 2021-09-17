# Header Parameter

from typing import Optional, List
from fastapi import FastAPI, Header

app = FastAPI()


"""
@app.get("/items/")
#async def read_items(user_agent: Optional[str] = Header(None)): #user_agent is a built-in
async def read_items(user_agent_custom: Optional[str] = Header(None, convert_underscores=False)): #convert_uderscores=false จะไม่ convert ชื่อ key ซึ่งก็คือ user_agent_custom แต่ถ้าเปลี่ยนกับ Built-in จะทำให้ Built-in นั้นเป็น Custom ทันที
    return {"User-Agent": user_agent_custom}
"""

# Duplicate headers
@app.get("/items/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}

@app.get("/authen/")
async def read_authen(Authorization: Optional[str] = Header(None)): # Authorization is a built-in can't override value
    #return {"Authorization": Authorization}
    return {"Authorization": Authorization.split(" ")[1]}