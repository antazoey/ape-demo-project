import click
from eth_account import Account
from eth_account.messages import encode_structured_data

from utils import get_account


DATA = {
    "domain": {
        "chainId": 1,
        "name": "Ether Mail",
        "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC",
        "version": "1",
    },
    "message": {
        "contents": "Hello, Bob!",
        "from": {
            "name": "Cow",
            "wallets": [
                "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
                "0xDeaDbeefdEAdbeefdEadbEEFdeadbeEFdEaDbeeF",
            ],
        },
        "to": [
            {
                "name": "Bob",
                "wallets": [
                    "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
                    "0xB0BdaBea57B0BDABeA57b0bdABEA57b0BDabEa57",
                    "0xB0B0b0b0b0b0B000000000000000000000000000",
                ],
            },
        ],
    },
    "primaryType": "Mail",
    "types": {
        "address": [],
        "EIP712Domain": [
            {"name": "name", "type": "string"},
            {"name": "version", "type": "string"},
            {"name": "chainId", "type": "uint256"},
            {"name": "verifyingContract", "type": "address"},
        ],
        "Group": [
            {"name": "name", "type": "string"},
            {"name": "members", "type": "Person[]"},
        ],
        "Mail": [
            {"name": "from", "type": "Person"},
            {"name": "to", "type": "Person[]"},
            {"name": "contents", "type": "string"},
        ],
        "Person": [
            {"name": "name", "type": "string"},
            {"name": "wallets", "type": "address[]"},
        ],
    },
}


def main():
    from ape import accounts

    account = accounts.load("gen0")
    message = encode_structured_data(primitive=DATA)
    signature = account.sign_message(message)
    signature_bytes = signature.encode_rsv()

    signer = Account.recover_message(message, signature=signature_bytes)
    if signer != account.address:
        click.echo(f"Signer resolves incorrectly, got {signer}, expected {account.address}.")
        return

    click.echo("Signature: " + signature.encode_vrs().hex())
