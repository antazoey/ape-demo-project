# @version ^0.3.3

owner: public(address)
myNumber: public(uint256)
prevNumber: public(uint256)

event NumberChange:
    prevNum: uint256
    newNum: indexed(uint256)

struct MyStruct:
    a: address
    b: bytes32

struct NestedStruct:
    t: MyStruct

@external
def __init__():
    self.owner = msg.sender

@external
def setNumber(num: uint256):
    assert msg.sender == self.owner, "!authorized"
    assert num != 5
    self.prevNumber = self.myNumber
    self.myNumber = num
    log NumberChange(self.prevNumber, num)

@view
@external
def getStruct() -> MyStruct:
    return MyStruct({a: msg.sender, b: block.prevhash})

@view
@external
def getNestedStruct() -> NestedStruct:
    return NestedStruct({t: MyStruct({a: msg.sender, b: block.prevhash})})

@pure
@external
def getEmptyList() -> DynArray[uint256, 1]:
    return []

@pure
@external
def getSingleItemList() -> DynArray[uint256, 1]:
    return [1]

@pure
@external
def getFilledList() -> DynArray[uint256, 3]:
    return [1, 2, 3]

@view
@external
def getAddressList() -> DynArray[address, 2]:
    return [msg.sender, msg.sender]

@pure
@external
def getMultipleValues() -> (uint256, uint256):
    return (123, 321)
