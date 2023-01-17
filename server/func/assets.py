import base64
import json
import os
from func.registry import load_and_check_registry_data


def encode_base64(string):
    return base64.b64encode(string.encode("utf-8")).decode("utf-8")


def get_assets(chain, network):
    assets = load_and_check_registry_data(chain, network, "assets")
    return assets


def get_asset_by_type(chain, network, asset_type):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset["type"] == asset_type]
    return asset


def get_asset_by_slug(chain, network, asset_slug):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if asset_slug in asset["slugs"]]
    return asset


def get_asset(chain, network, b64_asset_id):
    assets = load_and_check_registry_data(chain, network, "assets")
    asset = [asset for asset in assets if encode_base64(asset["id"]) == b64_asset_id][0]
    return asset


""" def get_asset_ibc(chain, network, hash):
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
 """
