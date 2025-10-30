# Import necessary modules
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model (used to validate incoming data for PUT requests)
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Define a GET endpoint for the root URL ('/')
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a GET endpoint that takes an item_id and optional query parameter q
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Define a PUT endpoint for updating an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}