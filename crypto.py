import requests

# Make a request to the CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol': 'BTC'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE'
}

response = requests.get(url, headers=headers, params=parameters)

# Extract the current value of the cryptocurrency from the API response
data = response.json()
price = data['data']['BTC']['quote']['USD']['price']

# Print the current value to the console
print(f'The current value of Bitcoin is ${price}')
