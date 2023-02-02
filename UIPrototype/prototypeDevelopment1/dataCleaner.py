"""
Data analysis for threat database
Libraries needed "pip install <>"
- pandas
- math

Author - Anderson Jolly
"""
import math
import pandas as pd

global df
df = pd.read_excel(r'UIPrototype\prototypeDevelopment1\threats.xlsx')  # read in the data
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


# MAPPING
# print(df['CATEGORY'].unique())
df['TYPE'] = df['TYPE'].map({'NETWORK': 0, 'LOCAL': 1})
df['SEVERITY'] = df['SEVERITY'].map({'LOW': 0, 'MEDIUM': 1, 'HIGH': 2})
df['CATEGORY'] = df['CATEGORY'].map(
    {'Execute Code': 0, 'Overflow': 1, 'Gain privileges': 2, 'Bypass a restriction or similar': 3,
     'Denial Of Service': 4, 'CSRF ': 5, 'File Inclusion ': 6, 'Cross Site Scripting': 7, 'Sql Injection': 8,
     'Obtain Information': 9, 'Directory traversal': 10, 'Http response splitting': 11})

# df['DATE'] = pd.cut(x=df['DATE'], bins=[1, 20, 40, 60,80, 100])
# df['DATE'] = df['DATE'].str.replace('T', '',)


# META DATA


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


def getAverageMetricFromCat(column: str, category: int):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mode()
    return mean


def getCountFromCat(category: str):
    temp = df.loc[df['CATEGORY'] == category].count()
    return temp[0]


# getAverageMetricFromCol("SCORE")
# print(getAverageMetricFromCat("SCORE", Overflow))
# print(getModalFromCol("CATEGORY"))
# print(getModalFromCol("TYPE"))
# print(getCountFromCat(Overflow))

# getTheatTypes()


