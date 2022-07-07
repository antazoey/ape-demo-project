import click
from ape import config, networks, project


# TODO: Parametrize and make a better example
def main():
    event_type = project.TestContractVy.NumberChange
    click.echo(f"Polling for new '{event_type}' logs...")

    for new_log in event_type.poll_logs():
        click.echo(new_log.newNum)
