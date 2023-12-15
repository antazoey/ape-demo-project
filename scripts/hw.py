import time
from functools import partial

import click
from ape import accounts, chain, convert, project
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import ConnectedProviderCommand
from ape.logging import logger
from eip712.messages import EIP712Message, EIP712Type
from eth_account.account import Account
from eth_account.messages import encode_defunct


class Person(EIP712Type):
    name: "string"  # type: ignore # noqa: F821
    wallet: "address"  # type: ignore # noqa: F821


class Mail(EIP712Message):
    _chainId_: "uint256" = 1  # type: ignore # noqa: F821
    _name_: "string" = "Ether Mail"  # type: ignore # noqa: F821
    _verifyingContract_: "address" = "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"  # type: ignore # noqa: F821 E501
    _version_: "string" = "1"  # type: ignore # noqa: F821

    sender: Person
    receiver: Person


ALICE_ADDRESS = "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"
BOB_ADDRESS = "0xB0B0b0b0b0b0B000000000000000000000000000"
TEST_SENDER = Person(name="Alice", wallet=ALICE_ADDRESS)
TEST_RECEIVER = Person("Bob", BOB_ADDRESS)
TEST_TYPED_MESSAGE = Mail(sender=TEST_SENDER, receiver=TEST_RECEIVER)


class HardwareCheck:
    def __init__(self, name, fn, signer) -> None:
        self.name = name
        self.fn = fn
        self.signer = signer

    def run(self):
        try:
            res = self.fn()
        except Exception as err:
            logger.log_debug_stack_trace()
            return False, str(err)

        return True, res


@click.command(cls=ConnectedProviderCommand)
@click.option("--max-fail", default=999)
@click.option("--account", default="ledger")
def cli(max_fail, account):
    logger.info("Starting simulation...")

    try:
        account = accounts.load(account)
    except IndexError:
        logger.error(f"'{account}''s plugin has likely failed to load :(")
        return

    net = chain.provider.network
    if net.is_dev:
        logger.info("Funding account...")
        requested_bal = convert("900 ETH", int)
        current_bal = account.balance
        difference = requested_bal - current_bal
        if difference > 0:
            try:
                account.balance += difference
            except NotImplementedError:
                funder = accounts.test_accounts[5]
                funder.transfer(account, difference)

        logger.success("Funding complete!")

    account_2 = funder

    check = partial(HardwareCheck, signer=funder.address)

    sign_msg = account.sign_message
    typed = TEST_TYPED_MESSAGE
    checks = [
        # check("Deploy - STATIC", lambda: account.deploy(project.FundMe, type=0)),
        # check("Deploy - DYNAMIC", lambda: account.deploy(project.FundMe, type=2)),
        # check("Transfer - STATIC", lambda: account.transfer(account_2, "1 gwei", type=0)),
        # check("Transfer - DYNAMIC", lambda: account.transfer(account_2, "1 gwei", type=2)),
        # check("Message - Legacy", lambda: sign_msg(encode_defunct(text="yo"))),
        # check("Message - Typed EIP712 obj", lambda: sign_msg(typed)),
        check("Message - Typed as SignableMessage", lambda: sign_msg(typed.signable_message)),
    ]

    results = []
    fail_ct = 0
    for check in checks:
        passed, res = check.run()
        passed_str = "PASSED" if passed else "FAILED"
        msg = f"{passed_str} - {check.name}"
        if not passed:
            msg = f"{msg} - {res}"
            fail_ct += 1
            if fail_ct == max_fail:
                break

        results.append(msg)
        time.sleep(4)

    for res in results:
        click.echo(res)

    logger.success("Simulation complete!")
