import base64
from func.registry import load_and_check_registry_data
from func.price import get_prices, get_price


def encode_base64(string):
    return base64.b64encode(string.encode("utf-8")).decode("utf-8")


def get_assets(chain, network):
    assets = load_and_check_registry_data(chain, network, "assets")
    assets = get_prices(assets)
    return assets


def get_assets_by_type(chain, network, asset_type):
    assets = load_and_check_registry_data(chain, network, "assets")
    assets = [asset for asset in assets if asset["type"] == asset_type]
    return assets


def get_assets_by_slug(chain, network, asset_slug):
    assets = load_and_check_registry_data(chain, network, "assets")
    assets = [asset for asset in assets if asset_slug in asset["slugs"]]
    return assets


def get_asset(chain, network, asset_id):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset["id"] == asset_id][0]
    return asset


def get_asset_ibc(chain, network, hash):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset["id"] == f"ibc/{hash}"][0]
    return asset


# Osmosis Assets


def get_asset_factory(chain, network, creator, symbol):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset["id"] == f"factory/{creator}/{symbol}"][
        0
    ]
    return asset


def get_asset_gamm(chain, network, pool_id):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset["id"] == f"gamm/pool/{pool_id}"][0]
    return asset
