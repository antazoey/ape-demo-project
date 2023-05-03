import click
from ape import accounts, project
from ape.cli import NetworkBoundCommand, network_option


@click.command(cls=NetworkBoundCommand)
@click.option("--address", help="The contract address, if already deployed.")
@network_option()
def cli(network, address):
    owner = accounts.load("metamask0")
    owner.set_autosign(True)

    if address:
        explorer = accounts.provider.network.explorer
        explorer.publish_contract(address)

    else:
        project.RunTheJules2Contract.deploy(owner, "Jules", "JUL", sender=owner, publish=True)
