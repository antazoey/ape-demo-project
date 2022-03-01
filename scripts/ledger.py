from cmath import log

import click
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
    funder.transfer(account, 900000000000000000000)
    logger.success("Funding complete!")
    assert account.balance

    # logger.info("Deploying smart contract using Static txn...")
    # contract = account.deploy(project.Fund, type=0)
    # logger.success("Smart contract deployed!")

    logger.info("Deploying smart contract using Dynamic txn...")
    contract = account.deploy(project.Fund)
    logger.success("Smart contract deployed!")

    logger.success("Simulation complete!")
