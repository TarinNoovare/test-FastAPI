from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/users/me")
async def read_current_user():
    return {"user": "current user"}

@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user": user_id}

