import uvicorn 
from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def main():
    return {"Message": 'Deploy API Success By.Nick'}

@app.post("/visual/")
async def login(data: str = Form(...)):
    return {"data": usernadatame}
