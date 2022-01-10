import requests
import json

headers = {"Accept": "application/json"}

def extract():
  eth_url = "https://api.bithumb.com/public/orderbook/ETH_KRW"
  response = requests.request("GET", eth_url, headers=headers)
  stats = json.loads(response.text)['data']['asks'][0]['price']
  ethPrice = int(stats)

  klay_url = "https://api.bithumb.com/public/orderbook/KLAY_KRW"
  response = requests.request("GET", klay_url, headers=headers)
  stats = json.loads(response.text)['data']['asks'][0]['price']
  klayPrice = int(stats)
  
  return ethPrice, klayPrice