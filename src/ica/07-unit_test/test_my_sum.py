from my_sum import *

def test_sum3_ints():
    """Tests the sum3 function with integer values."""
    assert sum3([5, 2, 8, -2, 6, 15]) == 15
    assert sum3([1, 2, 3, "h", "i"]) == 6
    assert sum3([-10, 0, 10]) == 0
    assert sum3([100, 200, 300, 400]) == 600

def test_sum3_floats():
    """Tests the sum3 function with float values."""
    assert sum3([1.5, 2.5, 5.0]) == 9.0
    assert sum3([10.0, -5.5, 0.5]) == 5.0
    assert sum3([-1.25, 0.0, 1.25, 99]) == 0.0
    assert sum3([0.5, 0.25, 0.75]) == 1.5