def string_of_nums(max_num):
    result_string = ""
    for i in range(1, max_num + 1):
        result_string = result_string + str(i) + " "
    return result_string
output = string_of_nums(10)
print(output)  # Should print "1 2 3 4 5 6 7 8 9 10 "