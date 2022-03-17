import ape

FUND_AMOUNT = 1000000000


def test_owner(fund_me_contract, owner):
    actual = fund_me_contract.owner()
    expected = owner.address
    assert actual == expected


def test_fund(fund_me_contract, funder):
    fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    actual = fund_me_contract.addressToAmountFunded(funder)
    assert actual == FUND_AMOUNT


def test_fund_muliple_times_in_a_row(fund_me_contract, funder):
    fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    assert fund_me_contract.addressToAmountFunded(funder) == FUND_AMOUNT * 3


def test_fund_emits_event(fund_me_contract, funder):
    receipt = fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    event_type = fund_me_contract.Fund
    fund_events = [e for e in event_type.from_receipt(receipt)]
    assert len(fund_events) == 1
    assert fund_events[0].funder == funder
    assert fund_events[0].amount == FUND_AMOUNT


def test_fund_zero_value(fund_me_contract, funder):
    with ape.reverts("Fund amount must be greater than 0."):
        fund_me_contract.fund(value=0, sender=funder)


def test_withdraw_not_owner(fund_me_contract, funder):
    with ape.reverts("!authorized"):
        fund_me_contract.withdraw(sender=funder)


def test_withdraw(fund_me_contract, owner, funder):
    fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)
    fund_me_contract.withdraw(sender=owner)
    assert fund_me_contract.addressToAmountFunded(funder) == 0


def test_withdraw_disabled(fund_me_contract, owner, funder):
    fund_me_contract.changeOnStatus(False, sender=owner)

    with ape.reverts():
        fund_me_contract.withdraw(sender=owner)

    with ape.reverts():
        fund_me_contract.fund(value=FUND_AMOUNT, sender=funder)

    with ape.reverts("!authorized"):
        fund_me_contract.changeOnStatus(False, sender=funder)

    fund_me_contract.changeOnStatus(True, sender=owner)
    fund_me_contract.withdraw(sender=owner)

    assert fund_me_contract.addressToAmountFunded(funder) == 0
