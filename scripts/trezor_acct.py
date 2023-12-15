from ape import accounts


def main():
    acct = accounts.load("teth0")
    print(acct.hd_path)
