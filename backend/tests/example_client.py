import requests
from typing import List, Optional
import time

BASE_URL = "http://127.0.0.1:8000/"
ALL_PRODUCTS_EXTENSION = "products"
PRODUCT_CANDLE_EXTENSION = "candles/{}/{}/{}/{}"


def get_product_ids() -> Optional[List[int]]:
    response = requests.get(BASE_URL + ALL_PRODUCTS_EXTENSION)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None


def get_candles(product_id: str, start_date: int, end_date: int, granularity: int) -> Optional[List[List[int]]]:
    response = requests.get(BASE_URL + PRODUCT_CANDLE_EXTENSION.format(
                                                                        product_id,
                                                                        start_date,
                                                                        end_date,
                                                                        granularity
                                                                        )
                            )
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
