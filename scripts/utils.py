from ape import accounts, networks, project
from ape.cli import get_user_selected_account


def deploy(*args, **kwargs):
    account = (
        _load_account_from_key("account", kwargs)
        or _load_account_from_key("sender", kwargs)
        or get_account(prompt="Select an account to deploy 'Fund.sol'")
    )
    return account.deploy(project.Fund, *args, **kwargs)


def _load_account_from_key(key: str, kwargs):
    if key in kwargs:
        account = kwargs.pop(key)
        if isinstance(account, str):
            return accounts.load(account)

        # Assume already loaded
        return account


def get_account(prompt=None):
    prompt = prompt or "Select an account"
    if is_test_network():
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def is_test_network() -> bool:
    network_name = networks.active_provider.name
    return network_name == "test"


def get_owner_and_funder():
    if is_test_network():
        owner = accounts.test_accounts[0]
        funder = accounts.test_accounts[1]
    else:
        owner = get_account(prompt="Select the contract owner account")
        funder = get_account(prompt="Select the contract funder account")

    return owner, funder
