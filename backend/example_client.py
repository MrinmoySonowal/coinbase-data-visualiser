import requests

BASE_URL = "http://127.0.0.1:8000/"
ALL_PRODUCTS_EXTENSION = "products"

def get_product_ids():
    responses = [requests.get(BASE_URL+ALL_PRODUCTS_EXTENSION) for _ in range(10)]
    if responses[0].status_code == 200:
        data = responses[0].json()
        return data
    else:
        print(f"Error: {responses[0].status_code}")
        return None
