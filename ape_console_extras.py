def ape_init_extras(accounts, config, networks):
    ecosystem = networks.provider.network.ecosystem.name
    network = networks.provider.network.name

    extras = {}

    try:
        if ecosystem in config.deployments:
            ecosystem_deployments = config.deployments[ecosystem]
            if network in ecosystem_deployments:
                network_deployments = ecosystem[network]
                deployments = [
                    d for d in network_deployments if d["contract_type"] == "TestContract"
                ]
                latest_address = deployments[-1]["address"]
                extras["test_contract_address"] = latest_address

        # Mimic fixtures
        extras = {
            "owner": accounts.test_accounts[0],
            "sender": accounts.test_accounts[1],
            **extras,
        }
    except Exception:
        pass

    return extras
