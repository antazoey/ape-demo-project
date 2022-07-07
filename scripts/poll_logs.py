import click
from ape import config, networks, project


# TODO: Parametrize and make a better example
def main():
    event_type = "NumberChange"
    contract_name = "TestContractSol"
    click.echo(f"Polling for new '{event_type}' logs...")

    ecosystem = networks.provider.network.ecosystem.name
    network = networks.provider.network.name.replace("-fork", "")
    contract_address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    contract_type = project.TestContractVy
    contract_instance = contract_type.at(contract_address)
    event_type = getattr(contract_instance, event_type)

    for new_log in event_type.poll_logs():
        click.echo(new_log.newNum)
