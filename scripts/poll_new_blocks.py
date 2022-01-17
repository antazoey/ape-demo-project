import click
from ape import chain


def main():
    for new_block in chain.blocks.poll_blocks():
        click.echo(new_block.number)
