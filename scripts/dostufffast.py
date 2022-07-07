from ape import networks


def main():
    for i in range(10000000):
        networks.provider.mine()
        num = networks.provider.get_block(i).number
        print(num)
