from ape.cli import AccountAliasPromptChoice
from ape import project


def main():
    account = AccountAliasPromptChoice().get_user_selected_account()
    account.deploy(project.Fund)
