from ape import accounts, project


def main():
    account = accounts.test_accounts[0]
    contract = project.dependencies["OpenZeppelin"].Governor
    account.deploy(contract)
