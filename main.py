from fastapi import FastAPI
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

class Item(BaseModel):
    name:str
    price:int

@app.get("/")
def home():
    return {"msg":"hellow"}

@app.put("/item/{itemId}")
def updatitem(itemId:int , item:Item):
    return {"item name":item.name,"itemId":itemId,"price":item.price}

@app.post("/item/{name}") 
def updatePrice(name:str,item:Item):
    print("item:",item)
    return {"itemId":name,"Price":item.price}

@app.get("/item/{itemId}")
def getItem(itemId:int,name:str,price:int):
    if(price == 0):
        return {"msg":"No price sent"}
    return {"itemId":itemId,"name":name,"price":price}


def generate_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

