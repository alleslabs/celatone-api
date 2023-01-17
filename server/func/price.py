import requests
from func.constants import COINGECKO_API_KEY


def get_prices(assets):
    slugs = [asset["coingecko"] for asset in assets if asset["coingecko"] is not None]
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(slugs)}&vs_currencies=usd&x_cg_pro_api_key={COINGECKO_API_KEY}"
    price_response = requests.get(url).json()
    for asset in assets:
        if asset["coingecko"] is not None:
            asset["price"] = price_response[asset["coingecko"]]["usd"]
    return assets


def get_price(asset):
    slug = asset["coingecko"]
    if slug is None:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={slug}&vs_currencies=usd&x_cg_pro_api_key={COINGECKO_API_KEY}"
        price_response = requests.get(url).json()
        asset["price"] = price_response[slug]["usd"]
    return asset
