# @version ^0.2.0

owner: public(address)
my_number: public(uint256)
prev_number: public(uint256)

event NumberChange:
    prev_num: uint256
    new_num: indexed(uint256)

struct Test:
    a: address
    b: bytes32

struct Nested:
    t: Test

@external
def __init__():
    self.owner = msg.sender

@external
def set_number(num: uint256):
    assert msg.sender == self.owner, "!authorized"
    assert num != 5
    self.prev_number = self.my_number
    self.my_number = num
    log NumberChange(self.prev_number, num)

@view
@external
def create_test_struct() -> Test:
    return Test({a: msg.sender, b: block.prevhash})

@view
@external
def create_nested_struct() -> Nested:
    return Nested({t: Test({a: msg.sender, b: block.prevhash})})
