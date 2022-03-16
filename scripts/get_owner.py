import click

from ._utils import deploy_fund_me


def main():
    contract = deploy_fund_me()
    owner = contract.owner()
    click.echo(owner)
