# Response File Content
# Must Install : pip3 install aiofile berfore

from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "readme.txt"
app = FastAPI()

@app.get("/")
async def main():
    return FileResponse(some_file_path)

@app.get("/download")
async def downalod():
    return FileResponse(path="./readme.txt", media_type='text/plain', filename=some_file_path)


@app.get("/download/image")
async def downalod():
    return FileResponse(path="./image.jpg", media_type='image/jpeg', filename="image.jpg")


