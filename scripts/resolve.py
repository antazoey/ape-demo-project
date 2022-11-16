import imp

import click
from ape import convert
from ape.types import AddressType


def main():
    click.echo(convert("juliya.eth", AddressType))
