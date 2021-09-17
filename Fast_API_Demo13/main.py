# Response HTML XML Redirect / Custom Response - HTML, Stream, File , Others on Fast API Dcoument (Advanced User Guide)

from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, RedirectResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()

# Response HTML
@app.get("/items/")
async def read_items():
    data =  """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>FastAPI</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=data)

# Response XML but need import Response 
@app.get("/legacy/")   
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")

# RedirectResponse
@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")



