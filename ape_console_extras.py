import json

import click
from ape.logging import logger


def ape_init_extras(accounts, project, config, networks):
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
        owner = accounts.test_accounts[0]
        logger.info(f"Deploying {project.FundMe} in ape_console_extras.py")
        contract = project.FundMe.deploy(sender=owner)
        extras = {
            "owner": owner,
            "sender": accounts.test_accounts[1],
            "fund_me": contract,
            "contract": contract,
            **extras,
        }

        # Add remaining accounts
        index = 2
        for acct in accounts.test_accounts[2:]:
            extras[f"acct{index}"] = acct
            index += 1

    except Exception as err:
        logger.error(err)
        pass

    extras["list_extras"] = lambda: click.echo(
        json.dumps({k: str(v) for k, v in extras.items() if k != "list_extras"}, indent=2)
    )
    return extras
