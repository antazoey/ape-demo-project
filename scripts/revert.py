"""
Deploy `Fund.sol` and make a request to it
that should revert.

This is for manual experience testing.
"""

from ape import accounts

from utils import deploy


def main():
    """
    Deploys a contract and forcibly cause a contract-logic revert.
    """
    owner = accounts.test_accounts[0]
    funder = accounts.test_accounts[1]
    contract = deploy(sender=owner)

    contract.fund(value=1000000000, sender=funder)

    # Attempting to withdraw from non-owner
    contract.withdraw(sender=funder)
