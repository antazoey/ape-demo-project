import ape


def test_set_number(vyper_contract, owner):
    receipt = vyper_contract.set_number(3, sender=owner)
    assert vyper_contract.my_number() == 3

    logs = [log for log in vyper_contract.NumberChange.from_receipt(receipt)]
    assert len(logs) == 1
    assert logs[0].prev_num == 0
    assert logs[0].new_num == 3


def test_set_number_not_owner(vyper_contract, funder):
    with ape.reverts("!authorized"):
        vyper_contract.set_number(3, sender=funder)


def test_set_number_reverts_when_five(vyper_contract, funder):
    with ape.reverts():
        vyper_contract.set_number(5, sender=funder)
