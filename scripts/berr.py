def main():
    import ape

    acct = ape.accounts.test_accounts[0]
    contract = ape.project.BuiltinErrorChecker.deploy(sender=acct)
    # contract.checkIndexOutOfBounds(sender=acct)
    contract.checkDivZero(0, sender=acct)
