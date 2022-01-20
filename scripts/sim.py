"""
Deploy `Fund.sol` and make a few normal requests to it.
"""

from .utils import deploy, get_owner_and_funder


def main():
    """
    Deploys the contract and makes a few calls.
    """
    owner, funder = get_owner_and_funder()
    contract = deploy(sender=owner)
    contract.fund(
        value=1000000000,
        sender=funder,
        max_priorty_fee=50000000000,
        max_fee=100000000000,
    )
    contract.withdraw(sender=owner)
