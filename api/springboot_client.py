import requests
from config import SPRINGBOOT_API_URL
from config import SPRINGBOOT_API_URL_NOBODY

def call_springboot_api(data):
    response = requests.post(SPRINGBOOT_API_URL, json={"data": data})
    return response.json()

def call_springboot_api_no_body():
    response = requests.post(SPRINGBOOT_API_URL_NOBODY)
    return response.status_code
