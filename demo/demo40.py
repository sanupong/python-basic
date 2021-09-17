# optional argument

from typing import Optional

def callAction(cmd:str, key:Optional[str]= None, priority:Optional[int]=0): #Optional ต้องอยู่ท้ายทั้งหมด
    print(cmd, priority, key)

callAction(cmd="login")
callAction(cmd="login", priority=1)
callAction(cmd="login", priority=1, key="1234")


