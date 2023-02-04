"""
Calculations and helper functions to calculate optimal solutions

Libraries needed "pip install <>"
- tabulate

Author - Viren Vadhvana
"""

from tabulate import tabulate

"""
Function to display the contents of the countermeasures database in a tabular format

Parameters: N/A
Returns: N/A
"""


def tabulateCountermeasures():
    table_data = []

    # Read and automatically close the file after use
    with open('countermeasures.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Countermeasure", "Covers", "Cost", "Effectiveness"]))


"""
Function to display the contents of the threats database in a tabular format

Parameters: N/A
Returns: N/A
"""


def tabulateThreats():
    table_data = []

    # Read and automatically close the file after use
    with open('threats.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Threat Name", "Severity Score"]))


"""
Function to display the countermeasures on a single line with all coverage and sorted on any column passed in

Parameters: rank
# To rank by Name, rank=0
# To rank by highest effectiveness against threat Alpha, rank=1
# To rank by highest effectiveness against threat Beta, rank=2
# To rank by highest effectiveness against threat Gamma, rank=3
# To rank by highest effectiveness against threat Delta, rank=4
# To rank by Cost, rank=5

Returns: N/A
"""


def tabulateOrderedCountermeasures(rank):
    # Read and automatically close the file after use
    with open('countermeasures.txt', 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()

    # Store as dictionary
    countermeasures = {}

    # Split data into correct headings
    for values in lines:
        cm, threat, cost, effectiveness = values.split()
        
        # Set up default values for all threats
        if cm not in countermeasures:
            countermeasures[cm] = {'Cost': int(cost), 'E_Alpha': 0, 'E_Beta': 0, 'E_Gamma': 0, 'E_Delta': 0}
            
        # Where a threat is covered, set the effectiveness
        countermeasures[cm]['E_' + threat] = float(effectiveness)

    # Add dictionary to new list to print
    tabulated = []
    for key, value in countermeasures.items():
        tabulated.append([key] + [value['E_Alpha'], value['E_Beta'], value['E_Gamma'], value['E_Delta'], value['Cost']])

    # Sort the result by the parameter
    # Reverse the list if showing effectiveness
    rev = False
    if 0 < rank < 5:
        rev = True

    def sortBy(cm):
        return cm[rank]

    tabulated = sorted(tabulated, key=sortBy, reverse=rev)

    print(tabulate(tabulated, headers=['Countermeasure', 'E_Alpha', 'E_Beta', 'E_Gamma', 'E_Delta', 'Cost']))


tabulateCountermeasures()
print()
tabulateThreats()
print()
tabulateOrderedCountermeasures(0)
print()
tabulateOrderedCountermeasures(1)
print()
tabulateOrderedCountermeasures(2)
print()
tabulateOrderedCountermeasures(3)
print()
tabulateOrderedCountermeasures(4)
print()
tabulateOrderedCountermeasures(5)
print()
