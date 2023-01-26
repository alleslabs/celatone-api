from func.registry import load_and_check_registry_data


def get_accounts(chain, network):
    accounts = load_and_check_registry_data(chain, network, "accounts")
    return accounts


def get_account(chain, network, account_address):
    accounts = load_and_check_registry_data(chain, network, "accounts")
    account = [
        account for account in accounts if account["address"] == account_address
    ][0]
    return account
