"""
For testing how networks handle various bad gas values.
"""

import click
from ape.exceptions import TransactionError

from ._utils import deploy_fund_me, get_account

TOO_HIGH = 999999999999999999


def main():
    account = get_account()
    try:
        # Specifying too low of a gas limit
        deploy_fund_me(sender=account, gas_limit=1)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too high of a gas limit
        deploy_fund_me(sender=account, gas_limit=TOO_HIGH)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too low of a gas price
        deploy_fund_me(sender=account, gas_price=1)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too high of a gas price
        deploy_fund_me(sender=account, gas_price=TOO_HIGH)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too high of a max_priority_fee
        deploy_fund_me(sender=account, max_priority_fee=TOO_HIGH)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too low of a max fee
        deploy_fund_me(sender=account, max_fee=1)
    except TransactionError as err:
        click.echo(str(err), err=True)

    try:
        # Specifying too high of a max_priority_fee
        deploy_fund_me(sender=account, max_fee=TOO_HIGH)
    except TransactionError as err:
        click.echo(str(err), err=True)
