from flask import send_file
import os

import func.codes as codes
import func.contracts as contracts
import func.accounts as accounts
import func.assets as assets
import func.projects as projects
import func.entities as entities
import func.balances as balances

from apiflask import APIFlask
from flask_cors import CORS

app = APIFlask(__name__, title="My API", version="1.0")
CORS(app)

app.config["SYNC_LOCAL_SPEC"] = True
app.config["LOCAL_SPEC_PATH"] = os.path.join(app.root_path, "openapi.json")
app.config["TAGS"] = [
    {
        "name": "Default",
        "description": "Default queries",
    },
    {
        "name": "Registry Data",
        "description": "Queries that uses data from the registry data JSONs",
    },
    {
        "name": "Registry Assets",
        "description": "Queries that uses data from the registry data asset images",
    },
    {
        "name": "External",
        "description": "Queries that uses also uses data from external sources",
    },
]

# Root


@app.route("/", methods=["GET"])
@app.doc(tags=["Default"])
def hello_world():
    return {"gm": "gm"}


# Codes


@app.route("/codes/<chain>/<network>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_codes(chain, network):
    """Get All Codes

    Returns a list of all the known codes based on the input chain and network
    """
    return codes.get_codes(chain, network)


@app.route("/codes/<chain>/<network>/<code_id>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_code(chain, network, code_id):
    """Get Code by ID

    Returns a specific code based on the input chain, network, and code_id
    """
    return codes.get_code(chain, network, code_id)


# Contracts


@app.route("/contracts/<chain>/<network>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_contracts(chain, network):
    """Get All Contracts

    Returns a list of all the known contracts based on the input chain and network"""
    return contracts.get_contracts(chain, network)


@app.route("/contracts/<chain>/<network>/<contract_address>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_contract(chain, network, contract_address):
    """Get Get Contract by ID

    Returns a specific contract based on the input chain, network, and contract_address"""
    return contracts.get_contract(chain, network, contract_address)


# Accounts


@app.route("/accounts/<chain>/<network>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_accounts(chain, network):
    """Get All Accounts

    Returns a list of all the known accounts based on the input chain and network
    """
    return accounts.get_accounts(chain, network)


@app.route("/accounts/<chain>/<network>/<account_address>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_account(chain, network, account_address):
    """Get Account by ID

    Returns a specific account based on the input chain, network, and account_address
    """
    return accounts.get_account(chain, network, account_address)


# Assets


@app.route("/assets/<chain>/<network>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_assets(chain, network):
    """Get All Assets

    Returns a list of all the known assets based on the input chain and network
    """
    return assets.get_assets(chain, network)


@app.route("/assets/<chain>/<network>/type/<asset_type>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_assets_by_type(chain, network, asset_type):
    """Get Assets by Type

    Returns a list of all the known assets based on the input chain, network, and asset_type
    """
    return assets.get_assets_by_type(chain, network, asset_type)


@app.route("/assets/<chain>/<network>/slug/<asset_slug>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_asset_by_slug(chain, network, asset_slug):
    return assets.get_assets_by_slug(chain, network, asset_slug)


@app.route("/assets/<chain>/<network>/<asset_id>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_asset(chain, network, asset_id):
    return assets.get_asset(chain, network, asset_id)


@app.route("/assets/<chain>/<network>/ibc/<hash>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_asset_ibc(chain, network, hash):
    return assets.get_asset_ibc(chain, network, hash)


@app.route("/assets/<chain>/<network>/factory/<creator>/<symbol>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_asset_factory(chain, network, creator, symbol):
    return assets.get_asset_factory(chain, network, creator, symbol)


@app.route("/assets/<chain>/<network>/gamm/pool/<pool_id>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_asset_gamm(chain, network, pool_id):
    return assets.get_asset_gamm(chain, network, pool_id)


# Projects


@app.route("/projects/<chain>/<network>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_projects(chain, network):
    return projects.get_projects(chain, network)


@app.route("/projects/<chain>/<network>/<project_id>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_project(chain, network, project_id):
    return projects.get_project(chain, network, project_id)


# Entities


@app.route("/entities", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_entities():
    return entities.get_entities()


@app.route("/entities/<entity_slug>", methods=["GET"])
@app.doc(tags=["Registry Data"])
def get_entity(entity_slug):
    return entities.get_entity(entity_slug)


# Balances


@app.route("/balances/<chain>/<network>/<account_address>", methods=["GET"])
@app.doc(tags=["Registry Data", "External"])
def get_balances(chain, network, account_address):
    return balances.get_balances(chain, network, account_address)


# Images


@app.route("/images/entities/<entity_slug>", methods=["GET"])
@app.doc(tags=["Registry Assets"])
def get_entity_image(entity_slug):
    return send_file(f"../registry/assets/entities/{entity_slug}.png")


@app.route("/images/assets/<asset_symbol>", methods=["GET"])
@app.doc(tags=["Registry Assets"])
def get_asset_image(asset_symbol):
    return send_file(f"../registry/assets/assets/{asset_symbol}.png")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
