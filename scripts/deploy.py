"""
Deploys the `Fund.sol` contract.
If not using the eth-tester network, you will be prompted to select an account.
"""

import click
from ape.cli import NetworkBoundCommand, network_option

from ._utils import deploy


@click.command(cls=NetworkBoundCommand)
@network_option()
@click.option("--contract", help="The contract to deploy.", default="FundMe")
def cli(network, contract):
    deploy(contract_type=contract)
    deploy(contract_type=contract)
