import ape


def test_no_portfolio(accounts):
    a = accounts[0]
    empty = a.deploy(ape.project.empty)
    with ape.reverts():
        empty.valuation(0)
