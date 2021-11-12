from ape import accounts, networks, project
from ape.cli import get_user_selected_account


def deploy(*args, **kwargs):
    account = (
        accounts.load(kwargs.pop("account")) if "account" in kwargs else get_account()
    )
    return account.deploy(project.Fund, *args, **kwargs)


def get_account():
    network_name = networks.active_provider.name
    if network_name == "test":
        return accounts.test_accounts[0]

    return get_user_selected_account(
        prompt_message="Select an account to deploy 'Fund'"
    )
