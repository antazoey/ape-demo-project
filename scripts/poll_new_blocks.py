import click
from ape import chain


def main():
    click.echo("Polling for new block...")
    for new_block in chain.blocks.poll_blocks():
        click.echo(new_block.number)
