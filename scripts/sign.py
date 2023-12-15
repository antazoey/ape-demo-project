def main():
    import ape

    a1 = ape.accounts.load("metamask0")
    a1.set_autosign(True, passphrase="123")
    a2 = ape.accounts.load("ledger")
    provider = ape.chain.provider
    ethy = provider.network.ecosystem

    for i in range(10):
        tx = ethy.create_transaction(sender=a1, receiver=a2)
        provider.prepare_tx(tx)
