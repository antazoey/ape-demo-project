import click
from ape import convert
from ape.exceptions import Abort

from ._utils import get_provider


def main():
    provider = get_provider()
    if provider.network.name != "mainnet":
        raise Abort("This script requires connecting to mainnet.")

    converted_val = convert("8.1 API3", int)
    click.echo(converted_val)

    converted_val = convert("8.234 LINK", int)
    click.echo(converted_val)
