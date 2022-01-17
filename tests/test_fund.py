import ape
import pytest

_FUND_AMOUNT = 1000000000


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def funder(accounts):
    return accounts[1]


@pytest.fixture
def contract(owner, project):
    return owner.deploy(project.Fund)


def test_owner(contract, owner):
    actual = contract.owner()
    expected = owner.address
    assert actual == expected


def test_fund(contract, funder):
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    actual = contract.addressToAmountFunded(funder)
    assert actual == _FUND_AMOUNT


def test_fund_muliple_times_in_a_row(contract, funder):
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    assert contract.addressToAmountFunded(funder) == _FUND_AMOUNT * 3


def test_fund_zero_value(contract, funder):
    with ape.reverts("Fund amount must be greater than 0."):
        contract.fund(value=0, sender=funder)


def test_withdraw_not_owner(contract, funder):
    with ape.reverts("!authorized"):
        contract.withdraw(sender=funder)


def test_withdraw(contract, owner, funder):
    contract.fund(value=_FUND_AMOUNT, sender=funder)
    contract.withdraw(sender=owner)
    assert contract.addressToAmountFunded(funder) == 0


def test_withdraw_disabled(contract, owner, funder):
    contract.changeOnStatus(False, sender=owner)

    with ape.reverts():
        contract.withdraw(sender=owner)

    with ape.reverts():
        contract.fund(value=_FUND_AMOUNT, sender=funder)

    with ape.reverts("!authorized"):
        contract.changeOnStatus(False, sender=funder)

    contract.changeOnStatus(True, sender=owner)
    contract.withdraw(sender=owner)

    assert contract.addressToAmountFunded(funder) == 0
