# @version ^0.2.0

owner: public(address)
my_number: public(uint256)
prev_number: public(uint256)

event NumberChange:
    prev_num: uint256
    new_num: uint256

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
