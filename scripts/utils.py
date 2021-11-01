from ape.cli import get_user_selected_account
from ape import project


def deploy():
    account = get_user_selected_account("Select an account to deploy 'Fund'")
    return account.deploy(project.Fund)
