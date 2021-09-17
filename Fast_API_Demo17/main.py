from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/share", StaticFiles(directory="static"), name="static") # /share คือ route ที่ให้คนเรียก API เห็น ส่วน directory="static" คือ folder ภายในของเรา

# ไม่ควรแชร์ ./ (Root Folder)
