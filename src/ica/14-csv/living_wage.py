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


def get_expensive_states(table):
    """
    Determines the five states with the highest required living wage.
    Returns a list of the five rows from the table.
    """
    sorted_table = sorted(table, key=lambda row: row['AnnualLivingWage'], reverse=True)
    return sorted_table[:5]


def annual_wage(hourly_wage):
    """
    Computes the annual wage for a family with two adults working full-time
    (40 hours/week, 52 weeks/year) at the given hourly wage.
    """
    return hourly_wage * 40 * 52 * 2


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


def print_gap_state_data(gap_states_list, table):
    """
    Prints a formatted table for states in the gap_states_list, showing
    their annual minimum wage earnings vs. their annual living wage.
    """
    print("\n--- Gap State Analysis ---")
    print(f"{'State':<20} {'Annual Min Wage':<20} {'Annual Living Wage':<20}")
    print("-" * 60)
    for state_name in gap_states_list:
        for row in table:
            if row['State'] == state_name:
                amw = annual_wage(row['HourlyMinimumWage'])
                alw = row['AnnualLivingWage']
                print(f"{row['State']:<20} ${amw:<19,.2f} ${alw:<19,.2f}")
                break


def vis_gaps(table):
    """
    Creates a bar chart showing the annual minimum wage and annual
    living wage for all 50 states.
    """
    sorted_table = sorted(table, key=lambda row: row['State'])
    state_abbrevs = [row['StateAbbrev'] for row in sorted_table]
    state_AMW = [annual_wage(row['HourlyMinimumWage']) for row in sorted_table]
    state_ALW = [row['AnnualLivingWage'] for row in sorted_table]

    plt.figure(figsize=(15.0, 7.0))
    bar_width = 0.4
    positions = np.arange(len(state_abbrevs))

    plt.bar(positions - bar_width / 2, state_AMW, bar_width, color='blue', label='Minimum Wage')
    plt.bar(positions + bar_width / 2, state_ALW, bar_width, color='green', label='Living Wage')

    plt.xlabel('States')
    plt.ylabel('Yearly Salary ($)')
    plt.title('Living and Minimum Wage In All States')
    plt.xticks(positions, state_abbrevs, rotation=0, fontsize=8)
    plt.legend()
    plt.tight_layout()
    plt.show()


def select_state_gaps(state_list, table):
    """
    Creates a bar chart showing the difference (the "gap") between the
    annual living wage and the annual minimum wage for a select list of states.
    """
    plot_states = []
    plot_gaps = []
    for row in table:
        if row['State'] in state_list or row['StateAbbrev'] in state_list:
            amw = annual_wage(row['HourlyMinimumWage'])
            alw = row['AnnualLivingWage']
            gap = alw - amw
            plot_states.append(row['StateAbbrev'])
            plot_gaps.append(gap)

    plt.figure(figsize=(10, 6))
    positions = np.arange(len(plot_states))
    plt.bar(positions, plot_gaps)
    plt.ylabel('Gap ($)')
    plt.title('Gap Between Living Wage and Annual Minimum Wage')
    plt.xticks(positions, plot_states)
    plt.tight_layout()
    plt.show()


def main():
    lw_fields, lw_data = read_living_wage_data('DataFiles/wages.csv')

    print("--- Testing get_state_living_wage ---")
    print(f"Living wage for Arkansas: ${get_state_living_wage('Arkansas', lw_data):,.2f}")
    print(f"Living wage for CA: ${get_state_living_wage('CA', lw_data):,.2f}")
    print(f"Living wage for Ontario: {get_state_living_wage('Ontario', lw_data)}")

    print("\n--- States at Federal Minimum Wage ($7.25) ---")
    low_wagers = get_low_wage_states(lw_data)
    print_table(low_wagers, ['State', 'HourlyMinimumWage'], 15)

    print("\n--- Top 5 Most Expensive States (by Living Wage) ---")
    expensive_states = get_expensive_states(lw_data)
    print_table(expensive_states, ['State', 'AnnualLivingWage'], 20)

    print("\n--- Finding Gap States ---")
    gap_states = get_gap_states(lw_data)
    print(f"There are {len(gap_states)} gap states.")

    print_gap_state_data(gap_states, lw_data)

    vis_gaps(lw_data)

    select_state_gaps(['CA', 'TX', 'MN', 'NY'], lw_data)


if __name__ == '__main__':
    main()