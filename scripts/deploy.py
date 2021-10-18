from ape.cli import get_user_selected_account
from ape import project


def main():
    account = get_user_selected_account()
    account.deploy(project.Fund)
