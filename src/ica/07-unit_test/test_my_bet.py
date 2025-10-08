from my_bet import *

def test_between():
  assert between(10, 0, 20) == True
  assert between(25, 10, 20) == False
  assert between(5.3, 6.7, 3.1) == False
  assert between(5.3, 3.1, 6.7) == True