import click
from ape import accounts, project
from ape.cli import NetworkBoundCommand, network_option
from ape.types import ContractLog


@click.command(cls=NetworkBoundCommand)
@network_option()
@click.option("--size", help="The amount of logs to generate.", default=101)
def cli(network, size):
    """Create and view a bunch of logs (sim)"""

    owner = accounts.test_accounts[0]
    contract_instance = owner.deploy(project.TestContractVy)

    min_range_size = 5
    if size <= min_range_size:
        raise ValueError(f"The range_size has to be > {min_range_size}.")

    numbers_to_set = [i for i in range(size, size * 2)]

    # Invoke transactions.
    for i in range(size):
        click.echo(f"Making transaction {i}")
        number = numbers_to_set[i]
        contract_instance.setNumber(number, sender=owner)

    # Collect logs.
    all_logs = [log for log in contract_instance.NumberChange]
    assert len(all_logs) == size

    expected_number = numbers_to_set[0]
    for log in all_logs:
        click.echo(f"Verifiying log with number {expected_number}")
        assert_log_values(log, expected_number)
        expected_number += 1


def assert_log_values(log: ContractLog, number: int):
    msg = f"The new number '{log.newNum}' is not expected '{number}'."
    assert log.newNum == number, msg
