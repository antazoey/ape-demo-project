import click
from ape.cli import ConnectedProviderCommand

from ._utils import deploy


@click.command(cls=ConnectedProviderCommand)
@click.option("--contract", help="The contract to deploy.", default="FundMe")
def cli(network, contract):
    contract = deploy(contract_type=contract)
    deploy_receipt = contract.receipt
    deploy_receipt.show_trace()
