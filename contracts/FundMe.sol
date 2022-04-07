// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

//import "@solidity-bytes-utils/contracts";

contract FundMe {
    address public owner;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    bool public enabled;

    constructor() {
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

    event Fund(address indexed funder, uint256 amount);

    function getSecret() public onlyOwner view returns(uint256 secret) {
        return 123;
    }

    function changeOnStatus(bool newValue) public onlyOwner {
        enabled = newValue;
    }

    function fund() public payable isOn {
        require(msg.value > 0, "Fund amount must be greater than 0.");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        emit Fund(msg.sender, msg.value);
    }

    function withdraw() public payable onlyOwner isOn {
        payable(msg.sender).transfer(address(this).balance);

        for (uint funderIndex=0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        funders = new address[](0);
    }
}
