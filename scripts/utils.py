from ape.cli import get_user_selected_account
from ape import accounts
from ape import networks
from ape import project


def deploy(gas_limit=None):
    account = get_account()
    return account.deploy(project.Fund, gas_limit=gas_limit)


def get_account():
    network_name = networks.active_provider.name
    if network_name == "test":
        breakpoint()
        return accounts[0]

    return get_user_selected_account(
        prompt_message="Select an account to deploy 'Fund'"
    )
