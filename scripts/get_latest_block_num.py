import click
from ape import networks


def main():
    num = networks.active_provider.get_block("latest").number
    styled_num = click.style(str(num), bold=True)
    click.echo(f"The current block number is {styled_num}.")
