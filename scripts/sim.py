"""
Deploy `Fund.sol` and make a few normal requests to it.
"""


from ape import accounts

from utils import deploy


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner = accounts.test_accounts[0]
    funder = accounts.test_accounts[1]
    contract = deploy(sender=owner)
    contract.fund(value=1000000000, sender=funder)
    contract.withdraw(sender=owner)
