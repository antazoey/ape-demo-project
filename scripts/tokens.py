from ape import convert
from ape.cli import Abort

from .utils import get_provider


def main():
    provider = get_provider()
    if provider.network.name != "mainnet":
        raise Abort("This script requires connecting to mainnet.")

    converted_val = convert("8.1 API3", int)
    print(converted_val)

    converted_val = convert("8.234 LINK", int)
    print(converted_val)
