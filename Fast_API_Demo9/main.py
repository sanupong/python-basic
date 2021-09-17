# Path Parameters and Numberic Validations

from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

# Declare metadata and alias query
"""
@app.get("/items/{item_id}") # วิธีเรียก http://localhost:8000/items/1?item-query=pong
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"), 
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
"""
# Order the parameters as you need
"""
@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str  # การใส่ * Asterisks จะทำให้ parameter ที่รับไม่สนใจลำดับ เพราะปกติ python จะให้ Optional ต้องอยู่ท้ายสุดเท่านั้น กรณีนี้ถ้าไม่มี * parameter q: str ต้องอยู่หน้า ก็จะใช้ได้
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
"""
# Number Validations: greater thand or equal
@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", lt=3), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
