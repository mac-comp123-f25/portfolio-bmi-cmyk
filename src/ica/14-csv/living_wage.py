"""
A program for analyzing the gap between minimum wage and living wage
across the 50 US states.

Completed by: Bridgette
"""
from helpers import *
import matplotlib.pyplot as plt
import numpy as np


def read_living_wage_data(filename):
    """
    Read the living wage CSV data from the given file. This function
    also converts the wage columns from strings to floating point numbers.
    """
    fields, table = read_csv(filename)
    for row in table:
        row['HourlyMinimumWage'] = float(row['HourlyMinimumWage'])
        row['AnnualLivingWage'] = float(row['AnnualLivingWage'])
    return fields, table


#ACTIVITY: get_state_living_wage
def get_state_living_wage(state_identifier, table):
    """
    Looks up a state by its full name or abbreviation (case-insensitive) and
    returns its annual living wage. Returns None if not found.
    """
    for row in table:
        if (state_identifier.lower() == row['State'].lower() or
                state_identifier.lower() == row['StateAbbrev'].lower()):
            return row['AnnualLivingWage']
    return None


# --------------------------------------

#ACTIVITY: get_low_wage_states
def get_low_wage_states(table):
    """
    Finds all states where the minimum wage is the federal minimum wage ($7.25).
    Returns a list of matching row dictionaries.
    """
    federal_min_wage = 7.25
    low_wage_list = []
    for row in table:
        if row['HourlyMinimumWage'] == federal_min_wage:
            low_wage_list.append(row)
    return low_wage_list


# ------------------------------------

#OPTIONAL ACTIVITY: get_expensive_states
def get_expensive_states(table):
    """
    Determines the five states with the highest required living wage.
    Returns a list of the five rows from the table.
    """
    # Sort the table by AnnualLivingWage in descending order
    # The key is a lambda function that extracts the wage for sorting
    sorted_table = sorted(table, key=lambda row: row['AnnualLivingWage'], reverse=True)

    # Return the first five elements of the sorted list
    return sorted_table[:5]


# ---------------------------------------------

#ACTIVITY: annual_wage
def annual_wage(hourly_wage):
    """
    Computes the annual wage for a family with two adults working full-time
    (40 hours/week, 52 weeks/year) at the given hourly wage.
    """
    hours_per_person_per_year = 40 * 52
    num_adults = 2
    total_annual_wage = hourly_wage * hours_per_person_per_year * num_adults
    return total_annual_wage


# -----------------------------

#ACTIVITY: get_gap_states
def get_gap_states(table):
    """
    Finds all states where a family of two adults earning minimum wage
    does not earn a living wage. Returns a list of the names of these "gap states".
    """
    gap_state_names = []
    for row in table:
        family_min_wage_annual = annual_wage(row['HourlyMinimumWage'])
        if family_min_wage_annual < row['AnnualLivingWage']:
            gap_state_names.append(row['State'])
    return gap_state_names


# --------------------------------

#OPTIONAL ACTIVITY: print_gap_state_data
def print_gap_state_data(gap_states_list, table):
    """
    Prints a formatted table for states in the gap_states_list, showing
    their annual minimum wage earnings vs. their annual living wage.
    """
    print("\n--- Gap State Analysis ---")
    # Print header
    print(f"{'State':<20} {'Annual Min Wage':<20} {'Annual Living Wage':<20} {'Gap':<20}")
    print("-" * 80)

    for state_name in gap_states_list:
        # Find the full data row for the state
        for row in table:
            if row['State'] == state_name:
                amw = annual_wage(row['HourlyMinimumWage'])
                alw = row['AnnualLivingWage']
                gap = alw - amw
                print(f"{row['State']:<20} ${amw:<19,.2f} ${alw:<19,.2f} ${gap:<19,.2f}")
                break  # Move to the next state name once found


# ------------------------------------------------

#OPTIONAL ACTIVITY: vis_gaps
def vis_gaps(table):
    """
    Creates a bar chart showing the annual minimum wage and annual
    living wage for all 50 states.
    """
    # Sort data by state name to ensure the plot is alphabetical
    sorted_table = sorted(table, key=lambda row: row['State'])

    # Initialize lists to hold the data for plotting
    state_abbrevs = []
    state_AMW = []  # Annual Minimum Wage
    state_ALW = []  # Annual Living Wage

    # Loop over the sorted table to populate the lists
    for row in sorted_table:
        state_abbrevs.append(row['StateAbbrev'])
        state_AMW.append(annual_wage(row['HourlyMinimumWage']))
        state_ALW.append(row['AnnualLivingWage'])

    #Plotting Code
    plt.figure(figsize=(15.0, 6.0))
    bar_width = 0.4
    opacity = 0.8
    positions = np.arange(len(state_abbrevs))

    plt.bar(positions - bar_width / 2, state_AMW, bar_width, alpha=opacity, color='cornflowerblue',
            label='Annual Minimum Wage')
    plt.bar(positions + bar_width / 2, state_ALW, bar_width, alpha=opacity, color='salmon', label='Annual Living Wage')

    plt.xlabel('States')
    plt.ylabel('Yearly Salary ($)')
    plt.title('Living Wage vs. Minimum Wage by State')
    plt.xticks(positions, state_abbrevs, rotation=90, fontsize=8)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# -----------------------------------

#OPTIONAL ACTIVITY: select_state_gaps
def select_state_gaps(state_list, table):
    """
    Creates a bar chart showing the difference (the "gap") between the
    annual living wage and the annual minimum wage for a select list of states.
    """
    plot_states = []
    plot_gaps = []

    for row in table:
        state_name = row['State']
        state_abbrev = row['StateAbbrev']
        if state_name in state_list or state_abbrev in state_list:
            amw = annual_wage(row['HourlyMinimumWage'])
            alw = row['AnnualLivingWage']
            gap = alw - amw
            plot_states.append(state_abbrev)
            plot_gaps.append(gap)

    plt.figure(figsize=(10, 6))
    positions = np.arange(len(plot_states))
    plt.bar(positions, plot_gaps, color='firebrick')

    plt.ylabel('Wage Gap ($)')
    plt.title('Gap Between Living Wage and Minimum Wage')
    plt.xticks(positions, plot_states)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# --------------------------------------------

# Main program
def main():
    lw_fields, lw_data = read_living_wage_data('DataFiles/wages.csv')
    print("--- Full Living Wage Data ---")
    print_table(lw_data, lw_fields, 15)

    # Sample calls for get_state_living_wage
    print("\n--- Testing get_state_living_wage ---")
    ark_liv_wage = get_state_living_wage('Arkansas', lw_data)
    print(f"Arkansas living wage is ${ark_liv_wage:,.2f}")
    cal_liv_wage = get_state_living_wage("CA", lw_data)
    print(f"California living wage is ${cal_liv_wage:,.2f}")
    ontario_wage = get_state_living_wage("Ontario", lw_data)
    print("Ontario living wage is", ontario_wage)

    # Sample calls for get_low_wage_states
    print("\n--- States at Federal Minimum Wage ($7.25) ---")
    low_wagers = get_low_wage_states(lw_data)
    print_table(low_wagers, lw_fields, 15)

    # Sample call for get_expensive_states (Optional)
    print("\n--- Top 5 Most Expensive States (by Living Wage) ---")
    expensive_states = get_expensive_states(lw_data)
    print_table(expensive_states, lw_fields, 15)

    # Sample calls for get_gap_states
    print("\n--- Finding Gap States ---")
    gap_states = get_gap_states(lw_data)
    print(f"There are {len(gap_states)} gap states.")
    print(gap_states)

    # Sample call for print_gap_state_data (Optional)
    print_gap_state_data(gap_states, lw_data)

    # Sample call for vis_gaps (Optional)
    # This will open a plot window. Close the window to continue.
    print("\nDisplaying visualization for all states...")
    vis_gaps(lw_data)

    # Sample call for select_state_gaps (Optional)
    print("\nDisplaying visualization for selected states...")
    select_state_gaps(['CA', 'TX', 'MN', 'FL', 'NY', 'WV'], lw_data)


if __name__ == '__main__':
    main()