# Import the pandas library and give it the standard alias 'pd'
import pandas as pd

# Define the name of our data file
csv_file_path = 'sample_sales.csv'

# Use a try-except block to handle the case where the file might not exist
try:
    # --- 1. Reading the CSV file into a DataFrame ---
    # A DataFrame is the primary data structure in pandas, like a table or spreadsheet.
    df = pd.read_csv(csv_file_path)
    print("✅ Successfully loaded the CSV file.")

    # --- 2. Displaying the data ---
    # .head() is a great way to preview the first few rows of your data.
    print("\n--- First 5 rows of the dataset ---")
    print(df.head())

    # --- 3. Performing a calculation on a column ---
    # You can select a single column (a 'Series') using square brackets.
    # .mean() is a built-in function to calculate the average.
    average_price = df['Price'].mean()
    print(f"\n--- Basic Calculation: Average Price ---")
    # We use :.2f to format the number to two decimal places, like currency.
    print(f"The average price of all products is: ${average_price:.2f}")

    # --- 4. Creating a new column based on existing data ---
    # We can create a new 'TotalSales' column by multiplying the Price and QuantitySold columns.
    df['TotalSales'] = df['Price'] * df['QuantitySold']
    print("\n--- Added a new 'TotalSales' column ---")
    print(df)

    # --- 5. Filtering the data ---
    # This is one of the most powerful features. We can select rows based on a condition.
    # Here, we create a new DataFrame containing only products from the 'Electronics' category.
    electronics_sales = df[df['Category'] == 'Electronics']
    print("\n--- Filtering: Showing only 'Electronics' products ---")
    print(electronics_sales)

    # --- 6. Aggregating filtered data ---
    # We can now perform calculations on our filtered data, like finding the total revenue from electronics.
    total_electronics_revenue = electronics_sales['TotalSales'].sum()
    print(f"\n--- Aggregation: Total revenue from Electronics ---")
    print(f"Total revenue from electronics sales: ${total_electronics_revenue:.2f}")


except FileNotFoundError:
    print(f"❌ Error: The file '{csv_file_path}' was not found.")
    print("Please make sure you have created 'sample_sales.csv' and it is in the same directory as this script.")