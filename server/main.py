from flask import Flask, send_file
import os

import func.codes as codes
import func.contracts as contracts
import func.accounts as accounts
import func.assets as assets
import func.projects as projects
import func.entities as entities
import func.balances as balances
import func.helper as helper

app = Flask(__name__)

# Root


@app.route("/")
def hello_world():
    return {"gm": "gm"}


# Codes


@app.route("/<chain>/<network>/codes")
def get_codes(chain, network):
    return codes.get_codes(chain, network)


@app.route("/<chain>/<network>/code/<code_id>")
def get_code(chain, network, code_id):
    return codes.get_code(chain, network, code_id)


# Contracts


@app.route("/<chain>/<network>/contracts")
def get_contracts(chain, network):
    return contracts.get_contracts(chain, network)


@app.route("/<chain>/<network>/contract/<contract_address>")
def get_contract(chain, network, contract_address):
    return contracts.get_contract(chain, network, contract_address)


# Accounts


@app.route("/<chain>/<network>/accounts")
def get_accounts(chain, network):
    return accounts.get_accounts(chain, network)


@app.route("/<chain>/<network>/account/<account_address>")
def get_account(chain, network, account_address):
    return accounts.get_account(chain, network, account_address)


# Assets


@app.route("/<chain>/<network>/assets")
def get_assets(chain, network):
    return assets.get_assets(chain, network)


@app.route("/<chain>/<network>/assets/type/<asset_type>")
def get_asset_by_type(chain, network, asset_type):
    return assets.get_asset_by_type(chain, network, asset_type)


@app.route("/<chain>/<network>/assets/slug/<asset_slug>")
def get_asset_by_slug(chain, network, asset_slug):
    return assets.get_asset_by_slug(chain, network, asset_slug)


@app.route("/<chain>/<network>/asset/<asset_id>")
def get_asset(chain, network, asset_id):
    return assets.get_asset(chain, network, asset_id)


# Projects


@app.route("/<chain>/<network>/projects")
def get_projects(chain, network):
    return projects.get_projects(chain, network)


@app.route("/<chain>/<network>/project/<project_id>")
def get_project(chain, network, project_id):
    return projects.get_project(chain, network, project_id)


# Entities


@app.route("/entities")
def get_entities():
    return entities.get_entities()


@app.route("/entity/<entity_slug>")
def get_entity(entity_slug):
    return entities.get_entity(entity_slug)


# Balances


@app.route("/<chain>/<network>/balances/<account_address>")
def get_balances(chain, network, account_address):
    return balances.get_balances(chain, network, account_address)


# Images


@app.route("/images/assets/<asset_symbol>")
def get_asset_image(asset_symbol):
    return send_file(f"../registry/assets/assets/{asset_symbol}.png")


@app.route("/images/entities/<entity_slug>")
def get_entity_image(entity_slug):
    return send_file(f"../registry/assets/entities/{entity_slug}.png")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
