# First example from instructions
def print_every_other(x):
    while x >= 0:  # x is the loop variable
        print(x)
        x = x - 2
    # when indentation stops, while loop is over
    print("Done!")


# Activity 1: print_every_fifth
def print_every_fifth(x):
    while x >= 0:
        print(x)
        x = x - 5
    print("Done!")


# Activity 2: Experimentation Comments
# Why are the two input lines repeated? The first pair of lines before the loop is the "priming read". It initializes the
# loop control variable (user_num) so that the `while` condition can be checked for
# the very first time. Without it, the program would crash with a NameError because
# `user_num` wouldn't exist when the `while` statement is first encountered.
# The second pair of lines inside the loop is the "update read". It gets the *next*
# value from the user. Without it, the value of `user_num` would never change inside
# the loop, leading to an infinite loop if the first number entered was not negative.

# Second example from instructions
def square_user_nums():
    # Initialize loop variable (priming read)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)
    while user_num >= 0:
        print(user_num, "squared is", user_num ** 2)
        # Update loop variable (update read)
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)


# Third example from instructions
def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # the loop variable
    total = 0  # the accumulator variable
    while curr_val < topNum:
        total = total + curr_val  # add next value to accumulator
        curr_val = curr_val + 1  # update the loop variable

    return total


# Activity 3: add_user_nums
def add_user_nums():
    sum_of_nums = 0
    user_num = int(input("Enter a number (0 to quit): "))
    while user_num != 0:
        sum_of_nums = sum_of_nums + user_num
        user_num = int(input("Enter a number (0 to quit): "))
    return sum_of_nums


# Fourth example from instructions
def nextWord(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline.
    """
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":  # if character is space, tab (\t), or newline (\n)
            break
        else:
            wordStr = wordStr + ch

    return wordStr


# Activity 4: square_user_nums2
def square_user_nums2():
    while True:
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)
        if user_num < 0:
            break
        print(user_num, "squared is", user_num ** 2)