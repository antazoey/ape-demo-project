# Ape Demo Project

This is a project that exists for demo-ing and manually testing ape.

**WARNING: This repo currently uses features in ape that still in development**

## Installation

First, clone this repo and change your working directory.

```bash
git clone git@github.com:unparalleled-js/ape-demo-project.git
cd ape-demo-project
```

Install the project's requirements:

```bash
pip install -r requirements-dev.txt 
```

Now, `ape` should be installed.

```bash
ape plugins install
```

## Contents

This project contains:

1. contracts
2. scripts
3. tests

### Contracts

To compile the contracts, do:

```bash
ape compile
```

This creates a `.build/` directory.

### Tests

To run the tests, do

```bash
ape test
```

### Scripts

Scripts are in the `scripts/` directory.

#### Deploy

To deploy the `Fund.sol` contract, run:

```bash
ape run deploy
```
