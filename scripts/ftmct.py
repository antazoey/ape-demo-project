from operator import ne

import click
from ape import networks


def main():
    provider = networks.provider
    network = provider.network
    assert network.ecosystem.name == "fantom", "Must use fantom"
    explorer = network.explorer
    assert explorer is not None, "Must have explorer (ape-etherscan) installed"
    address = "0x30Ac60fcbD79E03d51199BA87111b95C06e1E82F"
    contract_type = explorer.get_contract_type(address)
    click.echo(contract_type.name)
