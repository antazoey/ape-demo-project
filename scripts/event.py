import click
from ape import accounts, project
from ape.logging import LogLevel, logger


def echo_log(log):
    logger.success(f"Found event '{log.name}' with funder={log.funder} amount={log.amount}")


class main:
    logger.set_level(100)
    owner = accounts.test_accounts[0]
    funder = accounts.test_accounts[1]

    fund_me_contract = owner.deploy(project.FundMe)
    event_type = fund_me_contract.Fund
    event_name = event_type.name
    logger.set_level(LogLevel.INFO.value)

    click.echo(f"Triggering '{event_name}'...")
    receipt = fund_me_contract.fund(sender=funder, value=100)

    click.echo("Reading log from receipt...")
    log = [log for log in fund_me_contract.Fund.from_receipt(receipt)][0]
    echo_log(log)
    click.echo()

    click.echo("Reading log from event[index]...")
    log = fund_me_contract.Fund[-1]
    echo_log(log)
    click.echo()

    click.echo("Reading log from event.filter()[index]...")
    log = [log for log in fund_me_contract.Fund.filter(funder=funder)][0]
    echo_log(log)
