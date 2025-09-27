def add_tax(price, tax_rate):
    """
    This function takes a price and a tax rate and returns the total cost.
    """
    print("add_tax inputs: price=", price, ", tax_rate=", tax_rate)

    tax_amt = price * tax_rate

    print("Calculated tax_amt:", tax_amt)

    return price + tax_amt

print("--- Calculating tax for 25.99 ---")
total_cost = add_tax(25.99, 0.0725)
print("Final total cost:", total_cost)