from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse

some_file_path = "readme.txt"
app = FastAPI()

@app.get("/")
def main():
    def iterfile():  
        with open(some_file_path, mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="text/plain")

@app.get("/download")
def download():
    return FileResponse(path="./readme.txt", media_type='text/plain', filename=some_file_path)