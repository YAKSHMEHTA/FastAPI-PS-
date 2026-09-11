from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv("../.env")

API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

@app.get("/health")
def checkServer():
    return {"msg":"server is working"}

@app.get("/info/{loc}")
async def fetch(loc:str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={loc}")
        weather = res.json()
        data = {
            "location": loc,
            "region": weather["location"]["region"],
            "temperature": weather["current"]["temp_c"],
            "wind_kph": weather["current"]["wind_kph"],
            "humidity": weather["current"]["humidity"]
        }
        return data

    return {"msg":"failed"}