"""
Deploy `Fund.sol` and make a few normal requests to it.
"""

from ape import accounts

from ._utils import deploy, get_network_name, get_owner_and_funder


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner, funder = get_owner_and_funder()

    if get_network_name().endswith("-fork"):
        # Hack to give them money lolol
        financial_advice = accounts.test_accounts[0]
        financial_advice.transfer(owner, "1 ETH")
        financial_advice.transfer(funder, "1 ETH")

    contract = deploy(sender=owner)
    contract.fund(value=100, sender=funder)
    contract.fund(value=100, sender=funder)
    contract.withdraw(sender=owner)
