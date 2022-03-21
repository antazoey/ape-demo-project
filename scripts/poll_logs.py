import click
from ape import config, networks, project


def main():
    event_type = "NumberChange"
    contract_name = "TestContract"
    click.echo(f"Polling for new '{event_type}' logs...")

    ecosystem = networks.provider.network.ecosystem.name
    network = networks.provider.network.name
    network_deployments = config.deployments[ecosystem][network]
    deployments = [d for d in network_deployments if d["contract_type"] == contract_name]
    contract_address = deployments[0]["address"]
    contract_type = project.TestContract
    contract_instance = contract_type.at(contract_address)
    event_type = getattr(contract_instance, event_type)

    for new_log in event_type.poll_logs():
        click.echo(new_log.data)
