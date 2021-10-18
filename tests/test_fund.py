import ape

_FUND_AMOUNT = 1000000000


def test_fund(accounts, project):
    contract = accounts[0].deploy(project.Fund) 
    contract.fund(value=_FUND_AMOUNT, sender=accounts[1])
    assert contract.addressToAmountFunded(accounts[1].address) == _FUND_AMOUNT


def test_withdraw_not_owner(accounts, project):
    contract = accounts[0].deploy(project.Fund)

    with ape.reverts("!authorized"):
        contract.withdraw(sender=accounts[1])


def test_withdraw(accounts, project):
    contract = accounts[0].deploy(project.Fund) 
    contract.fund(value=_FUND_AMOUNT, sender=accounts[1])
    contract.withdraw(sender=accounts[0])
    assert contract.addressToAmountFunded(accounts[1].address) == 0
