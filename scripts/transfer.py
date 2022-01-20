from .utils import get_account


def main():
    sender = get_account("Which account is the sender")
    receiver = get_account("Which account is the receiver")
    sender.transfer(receiver, "1 gwei", required_confirmations=3)
