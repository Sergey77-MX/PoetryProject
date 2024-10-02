import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("PASSWORD")
# keys = os.getenv("API_KEY")
# headers = {keys: values}


def currency_conversion(transaction: Any) -> Any:
    """Функция конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return result["result"]
