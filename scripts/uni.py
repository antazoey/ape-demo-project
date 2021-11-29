from ape import Contract, project

UNISWAP_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

def main():
    uniswap = Contract(UNISWAP_ADDRESS)
    uniswap.swapExactETHForTokens
