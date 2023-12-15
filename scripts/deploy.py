"""
Deploys the `Fund.sol` contract.
If not using the eth-tester network, you will be prompted to select an account.
"""

import click
from ape.cli import ConnectedProviderCommand

from ._utils import deploy


@click.command(cls=ConnectedProviderCommand)
@click.option("--contract", help="The contract to deploy.", default="FundMe")
@click.option("--publish", is_flag=True)
def cli(network, contract, publish):
    deploy(contract_type=contract, publish=publish)
    # address = "0xc6112DB14f1a4f6D6Df3E770609B5f0f3B8B357a"
    # explorer = network.explorer
    # explorer.publish_contract(address)
