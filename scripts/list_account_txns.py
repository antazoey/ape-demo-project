import click
from ape import chain
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import Abort
from ape.logging import logger

from .utils import get_account, get_provider


def main():
    provider = get_provider()
    network_name = provider.network.name
    if network_name == LOCAL_NETWORK_NAME:
        raise Abort("Must use non-development network for this script.")

    if not provider.network.explorer:
        logger.warning(
            f"No explorer installed for network '{network_name}'. "
            "Only checking for ape-known transacitons."
        )
        do_abort = click.confirm("Abort, Ma'dam?")
        if do_abort:
            raise Abort("Operation aborted.")

    account = get_account()
    txns = chain.account_history[account]

    for txn in txns:
        click.echo(txn.txn_hash)
