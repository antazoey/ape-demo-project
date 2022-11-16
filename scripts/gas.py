import ape


def main():
    acct = ape.accounts.test_accounts[0]
    contract = acct.deploy(ape.project.FundMe)
