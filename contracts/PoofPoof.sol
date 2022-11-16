// SPDX-Licence-Identifier: MIT
pragma solidity 0.8.13;

interface ITruhuisAuction {
    function getAuctionStartTime(uint256 _tokenId) external view returns (uint256);

    function getIsResulted(uint256 _tokenId) external view returns (bool);

    function isAuctionApproved(address _account) external view returns (bool);
}
