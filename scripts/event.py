import click
from ape import accounts, project
from ape.logging import LogLevel, logger


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
    logs = fund_me_contract.Fund.from_receipt(receipt)

    for log in logs:
        click.echo(log.name)
        click.echo(log._funder)
        click.echo(log._amount)
