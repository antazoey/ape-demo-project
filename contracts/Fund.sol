// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Fund {
    address public owner;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    bool public enabled;

    constructor() public {
        owner = msg.sender;
        enabled = true;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "!authorized");
        _;
    }

    modifier isOn() {
        require(enabled);
        _;
    }

    function changeOnStatus(bool newValue) public onlyOwner {
        enabled = newValue;
    }

    function fund() public payable isOn {
        require(msg.value > 0, "Fund amount must be greater than 0.");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function withdraw() public payable onlyOwner isOn {
        msg.sender.transfer(address(this).balance);

        for (uint funderIndex=0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        funders = new address[](0);
    }
}
