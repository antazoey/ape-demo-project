import ape
import pytest

FUND_AMOUNT = 1000000000


def test_owner(solidity_contract, owner):
    actual = solidity_contract.owner()
    expected = owner.address
    assert actual == expected


def test_fund(solidity_contract, funder):
    solidity_contract.fund(value=FUND_AMOUNT, sender=funder)
    actual = solidity_contract.addressToAmountFunded(funder)
    assert actual == FUND_AMOUNT


def test_fund_muliple_times_in_a_row(solidity_contract, funder):
    solidity_contract.fund(value=FUND_AMOUNT, sender=funder)
    solidity_contract.fund(value=FUND_AMOUNT, sender=funder)
    solidity_contract.fund(value=FUND_AMOUNT, sender=funder)
    assert solidity_contract.addressToAmountFunded(funder) == FUND_AMOUNT * 3


@pytest.mark.parametrize("amount", (FUND_AMOUNT, FUND_AMOUNT * 2, FUND_AMOUNT * 3))
def test_fund_emits_event(solidity_contract, funder, amount):
    receipt = solidity_contract.fund(value=amount, sender=funder)
    events = receipt.events.filter(solidity_contract.Fund, funder=funder, amount=amount)
    assert len(events) == 1
    assert events[0].funder == funder
    assert events[0].amount == amount


def test_fund_zero_value(solidity_contract, funder):
    with ape.reverts():
        solidity_contract.fund(value=0, sender=funder)


def test_withdraw_not_owner(solidity_contract, funder):
    with ape.reverts("!authorized"):
        solidity_contract.withdraw(sender=funder)


def test_withdraw(solidity_contract, owner, funder):
    solidity_contract.fund(value=FUND_AMOUNT, sender=funder)
    solidity_contract.withdraw(sender=owner)
    assert solidity_contract.addressToAmountFunded(funder) == 0


def test_withdraw_disabled(solidity_contract, owner, funder):
    solidity_contract.changeOnStatus(False, sender=owner)

    with ape.reverts():
        solidity_contract.withdraw(sender=owner)

    with ape.reverts():
        solidity_contract.fund(value=FUND_AMOUNT, sender=funder)

    with ape.reverts("!authorized"):
        solidity_contract.changeOnStatus(False, sender=funder)

    solidity_contract.changeOnStatus(True, sender=owner)
    solidity_contract.withdraw(sender=owner)

    assert solidity_contract.addressToAmountFunded(funder) == 0


def test_get_secret(solidity_contract, owner):
    receipt = solidity_contract.getSecret(sender=owner)
    assert receipt

    if solidity_contract.provider.name == "hardhat":
        assert receipt.return_value == 123


def test_get_secrets(solidity_contract, owner):
    actual = solidity_contract.getSecrets(sender=owner)
    assert actual[0] == 123


def test_structs(solidity_contract, owner, addr, addr_fn, secret):
    actual = solidity_contract.getSenderStruct(sender=owner)
    assert actual.sender == owner
    assert False


@pytest.fixture(scope="session")
def addr():
    return "0xb5ed1ef2a90527b402cd7e7d415027cb94e1db4e"


@pytest.fixture
def addr_fn():
    return "0xb5ed1ef2a90527b402cd7e7d415027cb94e1db4e"


@pytest.fixture(params=[1, 2])
def secret(request):
    return request.param


def test_inter(secret, addr, addr_fn):
    assert False
