"""
Deploy `Fund.sol` and make a request to it
that should revert.

This is for manual experience testing.
"""

import click
from ape.exceptions import ContractLogicError

from .utils import deploy, get_owner_and_funder


def main():
    """
    Deploys a contract and forcibly cause a contract-logic revert.
    """
    owner, funder = get_owner_and_funder()
    contract = deploy(sender=owner)
    contract.fund(value=1000000000, sender=funder)

    try:
        # Attempting to withdraw from non-owner
        contract.withdraw(sender=funder)
    except ContractLogicError as err:
        click.echo(str(err), err=True)

    try:
        # Attempting to fund when disabled
        contract.changeOnStatus(False, sender=owner)
        contract.withdraw(sender=owner)
    except ContractLogicError as err:
        click.echo(str(err), err=True)
