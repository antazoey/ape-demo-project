import ape

FUND_AMOUNT = 1000000000


def test_owner(fund_contract, owner):
    actual = fund_contract.owner()
    expected = owner.address
    assert actual == expected


def test_fund(fund_contract, funder):
    fund_contract.fund(value=FUND_AMOUNT, sender=funder)
    actual = fund_contract.addressToAmountFunded(funder)
    assert actual == FUND_AMOUNT


def test_fund_muliple_times_in_a_row(fund_contract, funder):
    fund_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_contract.fund(value=FUND_AMOUNT, sender=funder)
    assert fund_contract.addressToAmountFunded(funder) == FUND_AMOUNT * 3


def test_fund_zero_value(fund_contract, funder):
    with ape.reverts("Fund amount must be greater than 0."):
        fund_contract.fund(value=0, sender=funder)


def test_withdraw_not_owner(fund_contract, funder):
    with ape.reverts("!authorized"):
        fund_contract.withdraw(sender=funder)


def test_withdraw(fund_contract, owner, funder):
    fund_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_contract.withdraw(sender=owner)
    assert fund_contract.addressToAmountFunded(funder) == 0


def test_withdraw_disabled(fund_contract, owner, funder):
    fund_contract.changeOnStatus(False, sender=owner)

    with ape.reverts():
        fund_contract.withdraw(sender=owner)

    with ape.reverts():
        fund_contract.fund(value=FUND_AMOUNT, sender=funder)

    with ape.reverts("!authorized"):
        fund_contract.changeOnStatus(False, sender=funder)

    fund_contract.changeOnStatus(True, sender=owner)
    fund_contract.withdraw(sender=owner)

    assert fund_contract.addressToAmountFunded(funder) == 0
