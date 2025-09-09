money = 732
print("Making change for", money, "cents:")
dollars = money // 100
money = money % 100
quarters = money // 25
money = money % 25
dimes = money // 10
money = money % 10
nickels = money // 5
money = money % 5
pennies = money
print(" Dollars:", dollars)
print(" Quarters:", quarters)
print(" Dimes:", dimes)
print(" Nickels:", nickels)
print(" Pennies:", pennies)