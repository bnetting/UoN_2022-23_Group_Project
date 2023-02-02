"""
Data analysis for threat database
Search Functionality Included
Libraries needed "pip install <>"
- pandas
- math

Author - Anderson Jolly
"""
import math
import pandas as pd

# TODO add data to excel
global df

# open excel database
df = pd.read_excel(r'threats.xlsx')  # read in the data
df.pop(df.columns[0])  # remove first column

NETWORK = 0
LOCAL = 1

LOW = 0
MEDIUM = 1
HIGH = 2

Execute_Code = 0
Overflow = 1
Gain_privileges = 2
Bypass_a_restriction_or_similar = 3
Denial_Of_Service = 4
CSRF = 5
File_Inclusion = 6
Cross_Site_Scripting = 7
Sql_Injection = 8
Obtain_Information = 9
Directory_traversal = 10
Http_response_splitting = 11


class Threat:
    def __init__(self, id, type, category, description, severity, score, exploitability, impact, date, link1, link2):
        self.cve = id
        self.type = type
        self.category = category
        self.description = description
        self.severity = severity
        self.score = score
        self.exploitability = exploitability
        self.impact = impact
        self.date = date
        self.link1 = link1
        self.link2 = link2


# MAPPING
def mapData():
    df['TYPE'] = df['TYPE'].map({'NETWORK': 0, 'LOCAL': 1})
    df['SEVERITY'] = df['SEVERITY'].map({'LOW': 0, 'MEDIUM': 1, 'HIGH': 2})
    df['CATEGORY'] = df['CATEGORY'].map(
        {'Execute Code': 0, 'Overflow': 1, 'Gain privileges': 2, 'Bypass a restriction or similar': 3,
         'Denial Of Service': 4, 'CSRF ': 5, 'File Inclusion ': 6, 'Cross Site Scripting': 7, 'Sql Injection': 8,
         'Obtain Information': 9, 'Directory traversal': 10, 'Http response splitting': 11})


def getTheatTypes():
    temp = (df['CATEGORY'].unique()).tolist()
    return temp


def getAverageMetricFromCol(column: str):  # Average metric of a column
    temp: int = df[column].mean()
    math.trunc(temp)
    return temp


def getModalFromCol(column: str):  # Most common metric from a column
    temp = df[column].mode()
    return temp


# DATA FROM THREAT TYPES
def getAverageMetricFromCat(column: str, category: int):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mean()
    return mean


def getModalMetricFromCat(column: str, category: int):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mode()
    return mean


def getCountFromCat(category: int):
    temp = df.loc[df['CATEGORY'] == category].count()
    return temp[0]


# SEARCHING

def searchByID(id: str):
    if id in df['ID'].values:
        row = df[df['ID'] == id]
        threat = Threat(row['ID'], row['TYPE'], row['CATEGORY'], row['DESCRIPTION'], row['SEVERITY'], row['SCORE'],
                        row['EXPLOITABILITY'], row['IMPACT'], row['DATE'], row['LINK'], row['OTHER'])
    else:
        print("NOT FOUND")
        return
    return threat


def filterByMetric(metric: str, value):
    threats = []
    row = df[df[metric] == value]
    numRows = row['ID'].count()
    for i in range(0, numRows):
        threat = Threat(row['ID'].iloc[i], row['TYPE'].iloc[i], row['CATEGORY'].iloc[i], row['DESCRIPTION'].iloc[i],
                        row['SEVERITY'].iloc[i], row['SCORE'].iloc[i],
                        row['EXPLOITABILITY'].iloc[i], row['IMPACT'].iloc[i], row['DATE'].iloc[i], row['LINK'].iloc[i],
                        row['OTHER'].iloc[i])
        threats.append(threat)

    return threats


def searchByDesc(text: str):
    threats = []
    row = df[df['DESCRIPTION'].str.contains(text)]
    numRows = row['ID'].count()
    for i in range(0, numRows):
        threat = Threat(row['ID'].iloc[i], row['TYPE'].iloc[i], row['CATEGORY'].iloc[i], row['DESCRIPTION'].iloc[i],
                        row['SEVERITY'].iloc[i], row['SCORE'].iloc[i],
                        row['EXPLOITABILITY'].iloc[i], row['IMPACT'].iloc[i], row['DATE'].iloc[i], row['LINK'].iloc[i],
                        row['OTHER'].iloc[i])
        threats.append(threat)

    return threats


# Testing

def main():
    mapData()
    getAverageMetricFromCol("SCORE")
    print(getAverageMetricFromCat("SCORE", Overflow))
    print(getModalFromCol("CATEGORY"))
    print(getModalFromCol("TYPE"))
    print(getCountFromCat(Overflow))

    print(getTheatTypes())

    searchByID("CVE-1999-0095")
    search = searchByDesc("SunOS")
    print(search[0].category)
    result = filterByMetric('SEVERITY', LOW)[1].score
    print(result)
    result = filterByMetric('IMPACT', 10)[1].exploitability
    print(result)


main()
