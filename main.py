from fastapi import FastAPI

app = FastAPI()

test_gay = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: float):
    return {"item_id": item_id}

