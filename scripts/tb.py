from ._utils import get_useful_receipt


def main():
    receipt = get_useful_receipt()
    receipt.show_traceback()
