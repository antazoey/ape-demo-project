from ape.cli import get_user_selected_account
from ape import project


def deploy():
    account = get_account("Select an account to deploy 'Fund'")
    return account.deploy(project.Fund)


def get_account(promt=None):
    return get_user_selected_account(prompt_message=promt)
