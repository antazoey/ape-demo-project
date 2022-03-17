import pytest


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def funder(accounts):
    return accounts[1]


@pytest.fixture
def solidity_contract(owner, project):
    return owner.deploy(project.FundMe)


@pytest.fixture
def vyper_contract(owner, project):
    return owner.deploy(project.TestContract)
