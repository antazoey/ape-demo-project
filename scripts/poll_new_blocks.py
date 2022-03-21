import click
from ape import chain


def main():
    click.echo("Polling for new blocks...")
    for new_block in chain.blocks.poll_blocks():
        click.echo(new_block.number)
