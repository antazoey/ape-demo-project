"""
Deploys the `Fund.sol` contract.
If not using the eth-tester network, you will be prompted to select an account.
"""

from .utils import deploy


def main():
    deploy()
