from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:int

@app.get("/")
def home():
    return {"msg":"hellow"}

@app.get("/item/{itemid}")
def getitem(itemid:int,q:str):
    return {"itemid":itemid,"q":q,}

@app.put("/item/{itemid}")
def updatitem(itemid:int , item:Item):
    return {"item name":item.name,"itemid":itemid}