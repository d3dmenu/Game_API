import uvicorn 
from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def main():
    return {"Message": 'Deploy API Success By.Nick'}

@app.post("/visual/")
async def login(data: str = Form(...)):
    return {"data": usernadatame}

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8080)