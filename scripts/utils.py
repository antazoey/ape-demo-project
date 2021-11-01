from ape.cli import get_user_selected_account
from ape import project


def deploy(gas_limit=None):
    account = get_user_selected_account(
        prompt_message="Select an account to deploy 'Fund'"
    )
    return account.deploy(project.Fund, gas_limit=gas_limit)
