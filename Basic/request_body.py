
# We can use Pydantic Models to get data from client 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

'''
    With this:
        1. We can get actual type of data we need
        2. Only we get needed data for processing, We do not get any extra dala which send from client
        3. Multiple use in diff endpoints
        ...
'''
@app.post("/items/")
async def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price
    }


# Request body + path + query parameters
'''
    You can also declare body, path and query parameters, all at the same time.
    FastAPI will recognize each of them and take the data from the correct place.
'''
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result








