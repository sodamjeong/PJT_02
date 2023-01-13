import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

info = requests.get(url).json()

print(info['data']['prev_closing_price'])