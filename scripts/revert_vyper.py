import ape


def main():
    account = ape.accounts.test_accounts[0]
    empty = account.deploy(ape.project.empty)
    empty.valuation(0)
