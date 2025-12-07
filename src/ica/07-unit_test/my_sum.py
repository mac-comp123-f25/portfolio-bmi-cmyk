def sum3(a_list):
    """
    Takes a list as input, checks that it has at least three numbers,
    and returns the sum of the first three elements.
    """
    assert type(a_list) in [list, tuple]
    assert len(a_list) >= 3
    assert type(a_list[0]) in [int, float]
    assert type(a_list[1]) in [int, float]
    assert type(a_list[2]) in [int, float]

    return a_list[0] + a_list[1] + a_list[2]
if __name__ == "__main__":
    print(sum3([5, 2, 8, -2, 6, 15]))
    print(sum3([1, 2, 3, "h", "i"]))
    print(sum3([1.5, 2.5, 5.0, 10]))