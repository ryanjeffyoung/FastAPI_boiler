from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder


app = FastAPI() #create FastAPI instance


@app.get("/")
async def root():
    resp = {"Message": "Hello World"}
    json_response = jsonable_encoder(resp)
    return json_response
