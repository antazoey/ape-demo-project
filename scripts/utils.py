from ape.cli import get_user_selected_account
from ape import accounts
from ape import networks
from ape import project


def deploy(*args, **kwargs):
    account = get_account()
    return account.deploy(project.Fund, *args, **kwargs)


def get_account():
    network_name = networks.active_provider.name
    if network_name == "test":
        return accounts.test_accounts[0]

    return get_user_selected_account(
        prompt_message="Select an account to deploy 'Fund'"
    )
