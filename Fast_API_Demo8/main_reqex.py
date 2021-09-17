# String Query RegularExpression
# Website built RegularExpression https://regexr.com/

from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")

async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")): # The Optional in Optional[str] is not used by FastAPI, but will allow your editor to give you better support and detect errors.
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
