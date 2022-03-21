import click
from ape import accounts, project
from ape.types import ContractLog

# NOTE: This test is VERY slow... Run only if you have 10 minutes to spare.
# Use higher numbers to avoid numbers related to other tests.
SIZE = 101


def main():
    owner = accounts.test_accounts[0]
    contract_instance = owner.deploy(project.TestContract)

    min_range_size = 5
    if SIZE <= min_range_size:
        raise ValueError(f"The range_size has to be > {min_range_size}.")

    numbers_to_set = [i for i in range(SIZE, SIZE * 2)]

    # Invoke 150 transactions.
    for i in range(SIZE):
        click.echo(f"Making transaction {i}")
        number = numbers_to_set[i]
        contract_instance.set_number(number, sender=owner)

    # Collect 150 logs.
    all_logs = [log for log in contract_instance.NumberChange.filter()]
    assert len(all_logs) == SIZE

    expected_number = numbers_to_set[0]
    for log in all_logs:
        click.echo(f"Verifiying log with number {expected_number}")
        assert_log_values(log, expected_number)
        expected_number += 1


def assert_log_values(log: ContractLog, number: int):
    msg = f"The new number '{log.new_num}' is not expected '{number}'."
    assert log.new_num == number, msg
