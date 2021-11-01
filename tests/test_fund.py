import pytest
import ape

_FUND_AMOUNT = 1000000000


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def funder(accounts):
    return accounts[1]


def test_fund(owner, funder, project):
    contract = owner.deploy(project.Fund) 
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    assert contract.addressToAmountFunded(funder.address) == _FUND_AMOUNT


def test_fund_muliple_times_in_a_row(owner, funder, project):
    contract = owner.deploy(project.Fund)
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    assert contract.addressToAmountFunded(funder.address) == _FUND_AMOUNT * 3


def test_fund_zero_value(owner, funder, project):
    contract = owner.deploy(project.Fund) 

    with ape.reverts("Fund amount must be greater than 0."):
        contract.fund(value=0, sender=funder)


def test_withdraw_not_owner(owner, funder, project):
    contract = owner.deploy(project.Fund)

    with ape.reverts("!authorized"):
        contract.withdraw(sender=funder)


def test_withdraw(owner, funder, project):
    contract = owner.deploy(project.Fund) 
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.withdraw(sender=owner)
    assert contract.addressToAmountFunded(funder.address) == 0
