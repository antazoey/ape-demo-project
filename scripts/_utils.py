from typing import Optional, Tuple, Union

import click
from ape import accounts, networks, project
from ape.api import AccountAPI, ProviderAPI, TestAccountAPI
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import get_user_selected_account
from ape.contracts.base import ContractInstance
from ape.exceptions import ApeException, ProviderError

Account = Union[AccountAPI, TestAccountAPI]


class ScriptError(ApeException):
    pass


def deploy(*args, **kwargs) -> ContractInstance:
    contract_type = kwargs.pop("contract_type", "FundMe")
    account = (
        _load_account_from_key("account", kwargs)
        or _load_account_from_key("sender", kwargs)
        or get_account(prompt=f"Select an account to deploy '{contract_type}'")
    )
    click.echo(f"Using account '{account.alias} - {account.address}'")
    contract_type = project.get_contract(contract_type)
    return account.deploy(contract_type, *args, **kwargs)


def _load_account_from_key(key: str, kwargs) -> Optional[Account]:
    if key not in kwargs:
        return None

    account = kwargs.pop(key)
    if isinstance(account, str):
        return accounts.load(account)

    # Assume already loaded
    return account


def get_account(prompt=None) -> Account:
    prompt = prompt or "Select an account"
    if is_test_network():
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def is_test_network() -> bool:
    test_networks = [LOCAL_NETWORK_NAME, "mainnet-fork"]
    provider = get_provider()
    network_name = provider.network.name
    return network_name in test_networks


def get_provider() -> ProviderAPI:
    provider = networks.active_provider
    if not provider:
        raise ProviderError("Not connected to a provider.")

    return provider


def get_owner_and_funder() -> Tuple[Account, Account]:
    if is_test_network():
        return accounts.test_accounts[0], accounts.test_accounts[1]
    else:
        return get_account(prompt="Select the contract owner account"), get_account(
            prompt="Select the contract funder account"
        )
