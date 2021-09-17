# Fast API : Advanced User Gude -> Additiona Response Status Code

from typing import Optional
from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}

@app.put("/items/{item_id}")
async def upsert_item(
    item_id: str, name: Optional[str] = Body(None), size: Optional[int] = Body(None)
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)  # สามารถกำหนด Status ได้โดย . หลัง Status หรือจะใส่ ตัวเลข และนิยามได้
        #return JSONResponse(status_code=404, content={"message": "Test Error"})
