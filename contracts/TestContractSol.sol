// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract TestContractSol {
    address public owner;
    uint256 public myNumber;
    uint256 public prevNumber;

    event NumberChange(uint256 prevNum, uint256 indexed newNum);

    struct MyStruct {
        address a;
        bytes32 b;
    }

    struct NestedStruct {
        MyStruct t;
    }

    constructor() {
        owner = msg.sender;
    }

    function setNumber(uint256 num) public {
        require(msg.sender == owner, "!authorized");
        require(num != 5);
        prevNumber = myNumber;
        myNumber = num;
        emit NumberChange(prevNumber, num);
    }

    function getStruct() public view returns(MyStruct memory) {
        return MyStruct(msg.sender, blockhash(block.number - 1));
    }

    function getNestedStruct() public view returns(NestedStruct memory) {
        return NestedStruct(getStruct());
    }

    function getEmptyList() public pure returns(uint256[] memory) {
        uint256[] memory data;
        return data;
    }

    function getSingleItemList() public pure returns(uint256[1] memory) {
        uint256[1] memory data = [uint256(1)];
        return data;
    }

    function getFilledList() public pure returns(uint256[3] memory) {
        uint256[3] memory data = [uint256(1), uint256(2), uint256(3)];
        return data;
    }

    function getAddressList() public view returns(address[2] memory) {
        address[2] memory data = [msg.sender, msg.sender];
        return data;
    }

    function getNamedSingleItem() public pure returns(uint256 foo) {
        return 123;
    }

    function getTupleAllNamed() public pure returns(uint256 foo, uint256 bar) {
        return (123, 321);
    }

    function getPartiallyNamedTuple() public pure returns(uint256 foo, uint256) {
        return (123, 321);
    }
}
