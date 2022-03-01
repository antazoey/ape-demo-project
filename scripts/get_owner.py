import click

from .utils import deploy


def main():
    contract = deploy()
    owner = contract.owner()
    click.echo(owner)
