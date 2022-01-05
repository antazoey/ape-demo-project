from ape import accounts, project


def main():
    a1 = accounts.test_accounts[0]
    a2 = accounts.test_accounts[1]
    c = a1.deploy(project.Fund)

    # TEST HERE
    r = c.fund([c, a2], value=100, sender=a1)
    print(r)
