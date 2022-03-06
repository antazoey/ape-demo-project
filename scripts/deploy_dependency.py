from ape import accounts, project


def main():
    account = accounts.test_accounts[0]
    contract = project.AccessControl
    account.deploy(contract)
