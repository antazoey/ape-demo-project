from ape import accounts, networks, project
from ape.cli import get_user_selected_account


def deploy(*args, **kwargs):
    account = (
        _load_account_from_key("account", kwargs)
        or _load_account_from_key("sender", kwargs)
        or get_account()
    )
    return account.deploy(project.Fund, *args, **kwargs)


def _load_account_from_key(key: str, kwargs):
    if key in kwargs:
        account = kwargs.pop(key)
        if isinstance(account, str):
            return accounts.load(account)

        # Assume already loaded
        return account


def get_account():
    network_name = networks.active_provider.name
    if network_name == "test":
        return accounts.test_accounts[0]

    return get_user_selected_account(
        prompt_message="Select an account to deploy 'Fund'"
    )
