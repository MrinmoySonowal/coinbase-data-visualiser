from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
import requests

app = FastAPI()

BASE_URL = "https://api.exchange.coinbase.com"
ALL_PRODUCTS_EXTENSION = "/products"
PRODUCT_CANDLE_EXTENSION = "/products/{}/candles?granularity={}&start={}&end={}"
MAX_RESPONSE_LEN_CANDLES = 300
ids = []


def get_all_ids(all_products_response: List[dict]) -> List[str]:
    product_ids = []
    for json_dicts in all_products_response:
        product_ids.append(json_dicts["id"])
    return sorted(product_ids)


@app.on_event("startup")
async def startup_event():
    global ids
    response = requests.get(BASE_URL + ALL_PRODUCTS_EXTENSION)
    if response.status_code == 200:
        data = response.json()
        ids = get_all_ids(data)
        return JSONResponse({"message": "Successful connection with API."})
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Unable to reach URL.")
    else:
        raise HTTPException(status_code=500, detail="Unable to connect API or retrieve data.")


@app.get("/products")
def get_all_products() -> JSONResponse:
    if ids:
        return JSONResponse(ids)
    else:
        return JSONResponse("Ids is not initialised, please re run server")


def get_candles_helper(product_id: str, start_timestamp: int, end_timestamp: int, granularity: int) -> List[int]:
    time_range = end_timestamp - start_timestamp
    if time_range > granularity * MAX_RESPONSE_LEN_CANDLES:
        raise Exception(
            f"Difference between start and end timestamp is {time_range}, must be less than or equal to 300")
    coinbase_endpoint = BASE_URL + PRODUCT_CANDLE_EXTENSION.format(product_id,
                                                                   granularity,
                                                                   start_timestamp,
                                                                   end_timestamp
                                                                   )
    response = requests.get(coinbase_endpoint)
    if response.status_code == 200:
        data = response.json()
        # for i in range(len(data[1:])):
        #
        return data
    else:
        return []


@app.get("/candles/{product_id}/{start_timestamp}/{end_timestamp}/{granularity}")
def get_candles(product_id: str, start_timestamp: int, end_timestamp: int, granularity: int) -> JSONResponse:
    current_end_timestamp = start_timestamp + MAX_RESPONSE_LEN_CANDLES*granularity
    if end_timestamp <= current_end_timestamp:
        candles = get_candles_helper(product_id, start_timestamp, end_timestamp, granularity)
    else:
        candles = get_candles_helper(product_id, start_timestamp, current_end_timestamp, granularity)
        # start_timestamp = current_end_timestamp+1
        # current_end_timestamp = min(current_end_timestamp+MAX_RESPONSE_LEN_CANDLES*granularity, end_timestamp)

    while current_end_timestamp <= end_timestamp:
        start_timestamp = current_end_timestamp + 1
        current_end_timestamp = min(current_end_timestamp + MAX_RESPONSE_LEN_CANDLES * granularity, end_timestamp)
        candles.extend(get_candles_helper(product_id, start_timestamp, current_end_timestamp, granularity))
        if current_end_timestamp == end_timestamp:
            break

    return JSONResponse(candles)
