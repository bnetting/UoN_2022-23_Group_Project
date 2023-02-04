from tabulate import tabulate


def tabulateCountermeasures():
    table_data = []
    with open('countermeasures.txt') as f:
        file_data = f.read()
        lines = file_data.splitlines()
        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Countermeasure", "Covers", "Cost", "Effectiveness"]))

def tabulateThreats():
    table_data = []
    with open('threats.txt') as f:
        file_data = f.read()
        lines = file_data.splitlines()
        for i in lines:
            values = i.split()
            table_data.append(values)

        print(tabulate(table_data, headers=["Threat Name", "Severity Score"]))


tabulateCountermeasures()
print()
tabulateThreats()