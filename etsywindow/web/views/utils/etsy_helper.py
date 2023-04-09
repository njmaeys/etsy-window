import os
import requests

def get_shop_data(store_name: str) -> dict:
    url = f"https://api.etsy.com/v3/application/shops?shop_name={store_name}"

    response = requests.get(url, headers={'X-Api-Key': os.environ.get('ETSY_API_KEY')})
    return response.json()
