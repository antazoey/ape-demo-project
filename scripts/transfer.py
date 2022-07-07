from webbrowser import get

import click
from ape import accounts
from ape.api.networks import LOCAL_NETWORK_NAME

from ._utils import account_loader, get_network_name


def main():
    network = get_network_name()
    if network == LOCAL_NETWORK_NAME or network.endswith("-fork"):
        sender = accounts.test_accounts[0]
        receiver = accounts.test_accounts[1]

    else:
        sender = account_loader.get_account("Which account is the sender")
        receiver = account_loader.get_account("Which account is the receiver")

    sender.transfer(receiver, "1 gwei")
    click.echo("done")
