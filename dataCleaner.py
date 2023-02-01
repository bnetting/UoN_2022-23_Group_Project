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
df = pd.read_excel(r'threats.xlsx')  # read in the data
df.pop(df.columns[0])  # remove first column


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
def getAverageMetricFromCat(column: str, category: str):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mean()
    return mean


def getAverageMetricFromCat(column: str, category: str):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mode()
    return mean


getAverageMetricFromCol("SCORE")
getAverageMetricFromCat("SCORE", "Overflow")
getModalFromCol("CATEGORY")
getTheatTypes()
