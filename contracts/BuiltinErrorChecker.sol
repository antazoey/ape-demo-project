// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.2;

contract BuiltinErrorChecker {
    uint256[] public _arr;

    constructor() {
        _arr = [1];
    }

    function checkIndexOutOfBounds() view public returns(uint256) {
        return _arr[2];
    }

    function checkDivZero(uint256 zero) pure public returns(uint256) {
        return 4 / zero;
    }
}
