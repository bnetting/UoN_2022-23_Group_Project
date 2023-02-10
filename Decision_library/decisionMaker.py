"""
Calculations and helper functions to calculate optimal solutions

Libraries needed "pip install <>"
- tabulate
- pulp

@:author Viren Vadhvana
"""

from tabulate import *
from pulp import *


def display_countermeasures():
    """
    Function to display the contents of the countermeasures database in a tabular format

    @:param None
    @:returns None
    """
    table_data = []

    # Read and automatically close the file after use
    with open('countermeasures.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        # Output as a table
        print(tabulate(table_data, headers=["Countermeasure", "Covers", "Cost", "Effectiveness"]))


def display_threats():
    """
    Function to display the contents of the threats database in a tabular format

    @:param None
    @:returns None
    """
    table_data = []

    # Read and automatically close the file after use
    with open('threats.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        # Output as a table
        print(tabulate(table_data, headers=["Threat Name", "Severity Score"]))


def tabulate_countermeasures():
    """
    Function to display the countermeasures on a single line with all coverage

    @:param None
    @:returns tabulated: a table of countermeasures with one countermeasure per line
    """
    # Read and automatically close the file after use
    with open('countermeasures.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

    # Store as dictionary
    countermeasures_dict = {}

    # Split data into correct headings
    for values in lines:
        cm, threat, cost, effectiveness = values.split()

        # Set up default values for all threats
        if cm not in countermeasures_dict:
            countermeasures_dict[cm] = {'Cost': int(cost), 'E_Alpha': 0.0, 'E_Beta': 0.0, 'E_Gamma': 0.0,
                                        'E_Delta': 0.0}

        # Where a threat is covered, set the effectiveness
        countermeasures_dict[cm]['E_' + threat] = float(effectiveness)

    # Add dictionary to new list to print
    tabulated = []
    for key, value in countermeasures_dict.items():
        tabulated.append([key] + [value['E_Alpha'], value['E_Beta'], value['E_Gamma'], value['E_Delta'], value['Cost']])

    # print("Tabulate function:")
    # print(tabulate(tabulated, headers=['Countermeasure', 'E_Alpha', 'E_Beta', 'E_Gamma', 'E_Delta', 'Cost']), '\n')

    return tabulated


def order_tabulated_countermeasures(table, rank):
    """
    Function to order a table by an input

    :param table: The table to be ordered
    :param rank: An integer representing the column header by which the data should be ordered

        # To rank by Name, rank=0
        # To rank by highest effectiveness against threat Alpha, rank=1
        # To rank by highest effectiveness against threat Beta, rank=2
        # To rank by highest effectiveness against threat Gamma, rank=3
        # To rank by highest effectiveness against threat Delta, rank=4
        # To rank by Cost, rank=5

    :return: tabulated: an ordered table
    """
    # Sort the result by the parameter
    # Reverse the list if showing effectiveness
    rev = False
    if 0 < rank < 5:
        rev = True

    def sort_by(cm):
        return cm[rank]

    tabulated = sorted(table, key=sort_by, reverse=rev)

    # print("Sorted function: ")
    # print(tabulate(tabulated, headers=['Countermeasure', 'E_Alpha', 'E_Beta', 'E_Gamma', 'E_Delta', 'Cost']), '\n')

    return tabulated


def optimise_budget_given_threats(budget, threats):
    """
    Function to calculate the best countermeasures to buy given a budget and the threats that need to be covered

    :param budget: The maximum value the user is willing to spend on countermeasures
    :param threats: A list of threats that need to be countered
    :return: solutions: A list containing the optimal countermeasures to buy

    """
    # Store the tabulated data in a list (Ordering is irrelevant)
    cm_data = order_tabulated_countermeasures(tabulate_countermeasures(), 0)

    # Map the necessary columns to lists
    countermeasures = []
    costs = []
    threats_data = []
    solutions = []
    for i in cm_data:
        countermeasures.append(i[0])
        costs.append(i[5])
        threat_data = []
        for j in range(len(threats)):
            if threats[j] < len(i):
                threat_data.append(i[threats[j]])
            else:
                threat_data.append(0)
        threats_data.append(threat_data)

    problem = LpProblem("Optimal Countermeasures", LpMaximize)

    # Create binary variables for each countermeasure
    countermeasure_vars = LpVariable.dicts("Countermeasure", countermeasures, 0, 1, LpBinary)

    # Objective function to maximise the sum of the chosen threat values
    threat_sum = 0
    for i in range(len(countermeasures)):
        for j in range(len(threats)):
            threat_sum += threats_data[i][j] * countermeasure_vars[countermeasures[i]]

    problem += threat_sum

    # Sum of the costs must be <= the budget
    cost_sum = 0
    for i in range(len(countermeasures)):
        cost_sum += costs[i] * countermeasure_vars[countermeasures[i]]

    problem += cost_sum <= budget

    problem.solve()

    print("Countermeasures to buy:")

    # Output optimal countermeasures to buy, or that there are no solutions
    no_solutions = True
    for solution in problem.variables():
        if solution.varValue == 1:
            solutions.append(solution.name)
            print(solution.name)
            no_solutions = False

    if no_solutions:
        print("You should consider increasing your spending budget as the current budget will not cover all threats")
        print("However, here is how your budget could be optimally spent: ")

    return solutions


"""
----------------------------------------------------------------------------------

                            !!!!TESTING THE FUNCTIONS!!!!

----------------------------------------------------------------------------------
"""

# print(order_tabulated_countermeasures(tabulate_countermeasures(), 5))

print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(100, [1, 3]))
print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(1000, [1, 3]))
print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(5000, [1, 3]))
print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(1000, [4]))
print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(1000, [1, 2, 3, 4]))
print("////////////////////////////////////////////////////////////////", optimise_budget_given_threats(750, [1, 2, 3, 4]))