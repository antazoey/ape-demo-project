from typing import Dict, Optional, Tuple, Union

import click
from ape import accounts, networks, project
from ape.api import AccountAPI, ProviderAPI, ReceiptAPI, TestAccountAPI
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import get_user_selected_account
from ape.contracts.base import ContractInstance
from ape.exceptions import ApeException, ProviderError

Account = Union[AccountAPI, TestAccountAPI]
TXN_HASH = "0x5e82d8eb827d98a896cab196cca4e6cf90cb78fb8a7b18c610769843abf7c92a"


class AccountLoader:
    cached_accounts: Dict[str, Account] = {}

    def load_account_from_key(self, key: str, kwargs) -> Optional[Account]:
        if key not in kwargs:
            return None

        if key in self.cached_accounts:
            return self.cached_accounts[key]

        account_arg = kwargs.pop(key)
        if isinstance(account_arg, str):
            # Load by alias
            account = accounts.load(account_arg)
            self.cached_accounts[key] = account
            return account

        # Assume already loaded
        return account_arg

    def get_account(self, prompt=None) -> Account:
        prompt = prompt or "Select an account"
        if is_test_network():
            return accounts.test_accounts[0]

        account = get_user_selected_account(prompt_message=prompt)
        self.cached_accounts[account.alias] = account
        return account


class ScriptError(ApeException):
    pass


def deploy(*args, **kwargs) -> ContractInstance:
    contract_type = kwargs.pop("contract_type", "FundMe")
    account = (
        account_loader.load_account_from_key("account", kwargs)
        or account_loader.load_account_from_key("sender", kwargs)
        or account_loader.get_account(prompt=f"Select an account to deploy '{contract_type}'")
    )
    click.echo(f"Using account '{account.alias} - {account.address}'")
    contract_type = project.get_contract(contract_type)
    return account.deploy(contract_type, *args, **kwargs)


account_loader = AccountLoader()


def is_test_network() -> bool:
    test_networks = [LOCAL_NETWORK_NAME, "mainnet-fork"]
    return get_network_name() in test_networks


def get_network_name() -> str:
    provider = get_provider()
    return provider.network.name


def get_provider() -> ProviderAPI:
    provider = networks.active_provider
    if not provider:
        raise ProviderError("Not connected to a provider.")

    return provider


def get_owner_and_funder() -> Tuple[Account, Account]:
    if is_test_network():
        return accounts.test_accounts[0], accounts.test_accounts[1]
    else:
        return account_loader.get_account(
            prompt="Select the contract owner account"
        ), account_loader.get_account(prompt="Select the contract funder account")


def get_useful_receipt() -> ReceiptAPI:
    return networks.provider.get_transaction(TXN_HASH)
