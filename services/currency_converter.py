import requests
import os

def convert_currency(amount, from_currency, to_currency):
    api_key = os.getenv("CURRENCY_API_KEY")
    url = f"https://currency-api.com/convert?from={from_currency}&to={to_currency}&amount={amount}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()["convertedAmount"]
