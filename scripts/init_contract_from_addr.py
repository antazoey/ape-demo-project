import click
from ape import accounts, project


def main():
    account = accounts.test_accounts[0]
    funder = accounts.test_accounts[1]

    contract = account.deploy(project.FundMe)

    click.echo("Call method from normal deployed contract...")
    contract.fund(value=1000000000, sender=funder)
    address = contract.address

    click.echo("Call method from contract initialized from address...")
    contract_from_address = project.FundMe.at(address)
    contract_from_address.fund(value=1000000000, sender=funder)
