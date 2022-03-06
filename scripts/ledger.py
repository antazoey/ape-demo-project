from ape import accounts, project
from ape.logging import logger


def main():
    logger.info("Starting simulation...")

    funder = accounts.test_accounts[5]

    try:
        account = accounts.load("main")
    except IndexError:
        logger.error("Ledger plugin has likely failed to load :(")
        return

    logger.info("Funding main account...")
    funder.transfer(account, "900 ETH")
    logger.success("Funding complete!")
    assert account.balance

    logger.info("Deploying smart contract using Static txn...")
    account.deploy(project.Fund, type=0)
    logger.success("Smart contract deployed!")

    logger.info("Deploying smart contract using Dynamic txn...")
    account.deploy(project.Fund, gas_limit=30029122)
    logger.success("Smart contract deployed!")

    logger.info("Returning funds to funder statically...")
    account.transfer(funder, "400 ETH", type=0)
    logger.success("Refunding complete!")
    assert account.balance

    logger.info("Returning funds to funder statically...")
    account.transfer(funder, "400 ETH")
    logger.success("Refunding complete!")
    assert account.balance

    logger.success("Simulation complete!")
