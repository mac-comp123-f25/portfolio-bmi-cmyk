def sum_range(start_val, end_val):
    cnt = 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x
    return cnt

print("Sum from 1 to 5 is:", sum_range(1, 5))  # Expected: 1+2+3+4+5 = 15
print("Sum from 3 to 3 is:", sum_range(3, 3))  # Expected: 3
print("Sum from 5 to 1 is:", sum_range(5, 1))  # Expected: 0 (the loop never runs)
print("Sum from -3 to -1 is:", sum_range(-3, -1))  # Expected: (-3)+(-2)+(-1) = -6