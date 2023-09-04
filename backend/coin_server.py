from fastapi import FastAPI, HTTPException
from typing import List
import requests

app = FastAPI()

BASE_URL = "https://api.exchange.coinbase.com/"
ALL_PRODUCTS_EXTENSION = "products"


def get_all_ids(all_products_response: str) -> List[str]:
    ids = []
    for json_dicts in all_products_response:
        ids.append(json_dicts["id"])
    return ids


def get_product_ticker(product_id: str) -> List[float]:
    pass


@app.get("/")
async def root():
    response = requests.get(BASE_URL + ALL_PRODUCTS_EXTENSION)
    if response.status_code == 200:
        data = response.json()
        ids = get_all_ids(data)
        return {"message": "Successful connection with API.", "ids": ids}
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Unable to reach URL.")
    else:
        raise HTTPException(status_code=500, detail="Unable to connect API or retrieve data.")
