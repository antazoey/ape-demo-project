import pytest


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def funder(accounts):
    return accounts[1]


@pytest.fixture
def fund_me_contract(owner, project):
    return owner.deploy(project.FundMe)


@pytest.fixture
def snake_contract(owner, project):
    return owner.deploy(project.Snake)
