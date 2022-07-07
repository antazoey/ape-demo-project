import click
from ape import accounts
from eip712.messages import EIP712Message, EIP712Type

# NOTE: Set this to the account you want to use in the test.
LEDGER_ACCOUNT_NAME = "TESTYO"


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


bob = Person("Bob", "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826")  # type: ignore
jane = Person("Jane", "0xB0B0b0b0b0b0B000000000000000000000000000")  # type: ignore
message = Mail(sender=bob, receiver=jane)  # type: ignore


def sign_typed_message():
    ledger_account = accounts.load(LEDGER_ACCOUNT_NAME)
    ledger_account.sign_message(message.body_data)


@click.command()
def cli():
    sign_typed_message()
