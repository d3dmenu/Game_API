import uvicorn 
import numpy as np
import warnings

from fastapi import FastAPI, Form

app = FastAPI()
warnings.simplefilter("ignore")

@app.get("/")
async def main():
    return {"Message": 'Deploy API Success By.Nick'}

@app.post("/visual/")
async def login(data: str = Form(...)):
    return {"data": usernadatame}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True)