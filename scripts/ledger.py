import click
from ape import accounts, chain, convert, project
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.logging import logger


class LedgerCheck:
    def __init__(self, name, fn) -> None:
        self.name = name
        self.fn = fn

    def run(self):
        try:
            return True, self.fn()
        except Exception as err:
            return False, str(err)


def main():
    logger.info("Starting simulation...")

    try:
        account = accounts.load("ledger")
    except IndexError:
        logger.error("Ledger plugin has likely failed to load :(")
        return

    net_name = chain.provider.network.name
    is_local = net_name == LOCAL_NETWORK_NAME or net_name.endswith("-fork")
    if is_local:
        logger.info("Funding account...")
        requested_bal = convert("900 ETH", int)
        current_bal = account.balance
        difference = requested_bal - current_bal
        if difference:
            try:
                account.balance += difference
            except NotImplemented:
                funder = accounts.test_accounts[5]
                funder.transfer(account, difference)

        logger.success("Funding complete!")

    checks = [
        LedgerCheck("Deploy - STATIC", lambda: account.deploy(project.FundMe, type=0)),
        LedgerCheck("Deploy - DYNAMIC", lambda: account.deploy(project.FundMe, type=1)),
        LedgerCheck("Transfer - STATIC", lambda: account.deploy(project.FundMe, type=0)),
        LedgerCheck("Transfer - DYNAMIC", lambda: account.deploy(project.FundMe, type=1)),
    ]

    results = []
    for check in checks:
        passed, res = check.run()
        passed_str = "PASSED" if passed else "FAILED"
        results.append(f"{passed_str} - {check.name}")

    for res in results:
        click.echo(res)

    logger.success("Simulation complete!")
