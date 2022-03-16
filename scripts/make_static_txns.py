"""
Does the same thing as `sim.py` except every transaction
uses the static type.

This is for manual experience testing.
"""

from ._utils import deploy_fund_me, get_owner_and_funder


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner, funder = get_owner_and_funder()
    contract = deploy_fund_me(sender=owner, type=0)
    contract.fund(value=1000000000, sender=funder, gas_price=1000000000)
    contract.withdraw(sender=owner, type=0)
