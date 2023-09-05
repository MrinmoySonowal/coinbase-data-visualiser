from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
import requests

app = FastAPI()

BASE_URL = "https://api.exchange.coinbase.com/"
ALL_PRODUCTS_EXTENSION = "products"
ids = []


def get_all_ids(all_products_response: str) -> List[str]:
    ids = []
    for json_dicts in all_products_response:
        ids.append(json_dicts["id"])
    return sorted(ids)



@app.on_event("startup")
async def startup_event():
    global ids
    response = requests.get(BASE_URL + ALL_PRODUCTS_EXTENSION)
    if response.status_code == 200:
        data = response.json()
        ids = get_all_ids(data)
        return {"message": "Successful connection with API."}
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Unable to reach URL.")
    else:
        raise HTTPException(status_code=500, detail="Unable to connect API or retrieve data.")


@app.get("/products")
def get_all_products():
    if ids:
        return JSONResponse(ids)
    else:
        return JSONResponse("Ids is not initialised, please re run server")