// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Fund {
    address public owner;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;

    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "!authorized");
        _;
    }

    function fund() public payable {
        require(msg.value > 0, "Fund amount must be greater than 0.");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);

        for (uint funderIndex=0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        funders = new address[](0);
    }
}
