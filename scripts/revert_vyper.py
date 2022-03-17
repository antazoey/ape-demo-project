import ape


def main():
    account = ape.accounts.test_accounts[0]
    empty = account.deploy(ape.project.TestContract)
    empty.valuation(0)
