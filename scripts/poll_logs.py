import click
from ape import config, networks, project


# TODO: Parametrize and make a better example
def main():
    event_type = project.TestContractVy.NumberChange
    click.echo(f"Polling for new '{event_type}' logs...")
    contract_address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    contract_type = project.TestContractVy

    for new_log in event_type.poll_logs():
        click.echo(new_log.newNum)
