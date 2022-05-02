from ape import accounts


def main():
    account = accounts.load("metamask0")
    account.unlock()
    account.unlock()
