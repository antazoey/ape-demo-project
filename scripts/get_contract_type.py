from click import echo

from ape import networks
from ape.exceptions import NetworkError


CONTRACT_ADDRESS = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
PROXY_CONTRACT_ADDRESS = "0xa354F35829Ae975e850e23e9615b11Da1B3dC4DE"


def main():
    explorer = networks.ethereum.mainnet.explorer
    if not explorer:
        raise NetworkError("Not connected to mainnet.")

    contract = explorer.get_contract_type(CONTRACT_ADDRESS)
    proxy = explorer.get_contract_type(PROXY_CONTRACT_ADDRESS)

    echo(contract.name)
    echo(proxy.name)
