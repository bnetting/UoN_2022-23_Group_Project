"""
Calculations and helper functions to calculate optimal solutions

Libraries needed "pip install <>"
- tabulate

@author: Viren Vadhvana
"""

from tabulate import *
from pulp import *


def tabulate_countermeasures():
    """
    Function to display the contents of the countermeasures database in a tabular format

    @:param: None
    @:returns: None
    """
    table_data = []

    # Read and automatically close the file after use
    with open('countermeasures.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Countermeasure", "Covers", "Cost", "Effectiveness"]))


def tabulate_threats():
    """
    Function to display the contents of the threats database in a tabular format

    @:param: None
    @:returns: None
    """
    table_data = []

    # Read and automatically close the file after use
    with open('threats.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Threat Name", "Severity Score"]))


def tabulate_ordered_countermeasures(rank):
    """
    Function to display the countermeasures on a single line with all coverage and sorted on any column passed in

    @param rank: An integer representing the column header by which the data should be ordered

       ` # To rank by Name, rank=0
        # To rank by highest effectiveness against threat Alpha, rank=1
        # To rank by highest effectiveness against threat Beta, rank=2
        # To rank by highest effectiveness against threat Gamma, rank=3
        # To rank by highest effectiveness against threat Delta, rank=4
        # To rank by Cost, rank=5`

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

    # Sort the result by the parameter
    # Reverse the list if showing effectiveness
    rev = False
    if 0 < rank < 5:
        rev = True

    def sort_by(cm):
        return cm[rank]

    tabulated = sorted(tabulated, key=sort_by, reverse=rev)

    print(tabulate(tabulated, headers=['Countermeasure', 'E_Alpha', 'E_Beta', 'E_Gamma', 'E_Delta', 'Cost']))

    return tabulated


def optimise_specific_budget(budget):  # threats needed - use #args for multiple
    """
    For a given budget, print the optimal solution to the threats Alpha and Gamma

    :param budget: Integer value representing the maximum costs the countermeasures can total
    :return: None
    """
    # Store the tabulated data in a list (Ordering is irrelevant)
    cm_data = tabulate_ordered_countermeasures(0)

    # Map the necessary columns to lists
    # TODO: Make this not hard coded
    countermeasures = []
    costs = []
    e_alpha = []
    e_gamma = []
    for i in cm_data:
        countermeasures.append(i[0])
        costs.append(i[5])
        e_alpha.append(i[1])
        e_gamma.append(i[3])

    problem = LpProblem("Optimal Countermeasures", LpMaximize)

    # Create binary variables for each countermeasure
    countermeasure_vars = LpVariable.dicts("Countermeasure", countermeasures, 0, 1, LpBinary)

    # Objective function to maximise the sum of the e_alpha and e_gamma values
    # Calculate the sum of alpha and gamma for each countermeasure
    alpha_sum = 0
    for i in range(len(countermeasures)):
        alpha_sum += e_alpha[i] * countermeasure_vars[countermeasures[i]]

    gamma_sum = 0
    for i in range(len(countermeasures)):
        gamma_sum += e_gamma[i] * countermeasure_vars[countermeasures[i]]

    problem += alpha_sum + gamma_sum

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
            print(solution.name)
            no_solutions = False

    if no_solutions:
        print("You should consider increasing your spending budget as the current budget will not cover all threats")
        print("However, here is how your budget could be optimally spent: ")


"""
----------------------------------------------------------------------------------

                            !!!!TESTING THE FUNCTIONS!!!!

----------------------------------------------------------------------------------
"""

tabulate_countermeasures()
print()
tabulate_threats()
print()
tabulate_ordered_countermeasures(0)
print()
tabulate_ordered_countermeasures(1)
print()
tabulate_ordered_countermeasures(2)
print()
tabulate_ordered_countermeasures(3)
print()
tabulate_ordered_countermeasures(4)
print()
tabulate_ordered_countermeasures(5)
print()
optimise_specific_budget(100)
print()
optimise_specific_budget(1000)
print()
optimise_specific_budget(5000)
