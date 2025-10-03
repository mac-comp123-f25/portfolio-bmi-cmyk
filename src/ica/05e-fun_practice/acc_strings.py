def copy_str(string, num_times):
    ans_str = ""

    for x in range(num_times):
        ans_str = ans_str + string
        print("Inside the loop, ans_str is now:", ans_str)
    return ans_str

print("--- Calling copy_str('Go! ', 3) ---")
final_result = copy_str("Go! ", 3)
print("The final returned string is:", final_result)