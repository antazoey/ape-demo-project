from ape import chain
import click

from utils import get_account


def main():
    account = get_account()
    txns = chain.account_history[account]
    for txn in txns:
        click.echo(txn)
