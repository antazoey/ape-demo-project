def ape_init_extras(config, networks):
    ecosystem = networks.provider.network.ecosystem.name
    network = networks.provider.network.name
    network_deployments = config.deployments[ecosystem][network]
    deployments = [d for d in network_deployments if d["contract_type"] == "TestContract"]
    latest_address = deployments[-1]["address"]

    return {
        "test_contract_address": latest_address,
    }
