"""
Does the same thing as `sim.py` except every transaction
uses the static type.

This is for manual experience testing.
"""

from .utils import deploy, get_owner_and_funder, get_provider


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner, funder = get_owner_and_funder()
    contract = deploy(sender=owner, type=0)
    contract.fund(value=1000000000, sender=funder, gas_price=1000000000)
    contract.withdraw(sender=owner, type=0)
