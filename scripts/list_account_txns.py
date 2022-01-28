import click
from ape import chain

from .utils import get_account, get_provider


def main():
    if get_provider().network.name == "development":
        raise Exception("Must use non-development network for this script.")

    account = get_account()
    txns = chain.account_history[account]
    for txn in txns:
        click.echo(txn.txn_hash)
