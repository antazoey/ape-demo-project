from ape import accounts

from utils import deploy


"""
Does the same thing as `sim.py` except every transaction
uses the static type.

This is for manual experience testing.
"""


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner = accounts.test_accounts[0]
    funder = accounts.test_accounts[1]
    contract = deploy(sender=owner, type=0)
    contract.fund(value=1000000000, sender=funder, gas_price=769470254)
    contract.withdraw(sender=owner, type=0)
