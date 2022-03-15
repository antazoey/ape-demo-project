import ape


def test_set_number(snake_contract, owner):
    snake_contract.set_number(3, sender=owner)
    assert snake_contract.my_number() == 3


def test_set_number_not_owner(snake_contract, funder):
    with ape.reverts("!authorized"):
        snake_contract.set_number(3, sender=funder)


def test_set_number_reverts_when_five(snake_contract, funder):
    with ape.reverts():
        snake_contract.set_number(5, sender=funder)
