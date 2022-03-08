"""
Deploys the `Fund.sol` contract.
If not using the eth-tester network, you will be prompted to select an account.
"""

import click
from ape.cli import NetworkBoundCommand, network_option

from ._utils import deploy as deploy


@click.command(cls=NetworkBoundCommand)
@network_option()
def cli(network):
    deploy()
