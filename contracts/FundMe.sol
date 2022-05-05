// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

//import "@solidity-bytes-utils/contracts";

contract FundMe {
    address public owner;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    bool public enabled;

    error InsufficientFund(uint256 given, uint256 required);

    struct Book { 
      string title;
      string author;
      uint book_id;
    }

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

    function getSecrets() public onlyOwner view returns(uint256 secret1, uint256 secret2) {
        return (123, 321);
    }

    function getSecretsNotAllNamed() public onlyOwner view returns(uint256, uint256 secret2) {
        return (123, 321);
    }

    function changeOnStatus(bool newValue) public onlyOwner {
        enabled = newValue;
    }

    function fund() public payable isOn {
        if (msg.value <= 0) {
            revert InsufficientFund(msg.value, 1);
        }
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        emit Fund(msg.sender, msg.value);
    }

    function getBook() public pure returns(Book memory) {
        return Book('Learn Python', 'TP', 1);
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
