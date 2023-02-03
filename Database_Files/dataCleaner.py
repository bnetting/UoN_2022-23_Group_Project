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
# TODO getters and setters for values
global df

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

df = pd.read_excel('threats.xlsx', engine='openpyxl', index_col=0)


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

    def getID(self):
        return self.cve

    def getType(self):
        return self.type

    def getCategory(self):
        return self.category

    def getDescription(self):
        return self.description

    def getSeverity(self):
        return self.severity

    def getScore(self):
        return self.score

    def getExploitability(self):
        return self.exploitability

    def getImpact(self):
        return self.impact

    def getDate(self):
        return self.date

    def getLink1(self):
        return self.link1

    def getLink2(self):
        return self.link2

    def addEntry(self, df):
        df2 = pd.DataFrame(
            {'ID': [self.cve], 'TYPE': [self.type], 'CATEGORY': [self.category], 'DESCRIPTION': [self.description],
             'SEVERITY': [self.severity], 'SCORE': [self.score], 'EXPLOITABILITY': [self.exploitability],
             'IMPACT': [self.impact], 'DATE': [self.date], 'LINK': [self.link1], 'OTHER': [self.link2]})
        print(df2)
        df = df.append(df2, ignore_index=True)
        writer = pd.ExcelWriter('threats.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=True, header=True)
        writer.close()
        print("WRITE SUCCESS")

        print("SUCCESS")


# MAPPING
def mapData():
    df['TYPE'] = df['TYPE'].map({'NETWORK': 0, 'LOCAL': 1})
    df['SEVERITY'] = df['SEVERITY'].map({'LOW': 0, 'MEDIUM': 1, 'HIGH': 2})
    df['CATEGORY'] = df['CATEGORY'].map(
        {'Execute Code': 0, 'Overflow': 1, 'Gain privileges': 2, 'Bypass a restriction or similar': 3,
         'Denial Of Service': 4, 'CSRF ': 5, 'File Inclusion ': 6, 'Cross Site Scripting': 7, 'Sql Injection': 8,
         'Obtain Information': 9, 'Directory traversal': 10, 'Http response splitting': 11})


def getThreatTypes():
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
    print(getAverageMetricFromCol("EXPLOITABILITY"))
    print(getAverageMetricFromCat("SCORE", Overflow))
    print(getModalFromCol("CATEGORY"))
    print(getModalFromCol("TYPE"))
    print(getCountFromCat(Overflow))
    print(getThreatTypes())

    print(searchByID("CVE-1999-0095").getDate())
    search = searchByDesc("SunOS")
    print(search[0].getCategory())
    #  result = filterByMetric('SEVERITY', LOW)[0].score
    #   print(result)
    result = filterByMetric('IMPACT', 10)[0].exploitability
    print(result)

    print("------------\n")

    new = Threat("hello", "NETWORK", "MITM", 'messed up mate', 'MEDIUM', 4.5, 6.2, 4.2, '2023', 'df', 'fe')
    new.addEntry(df)
    print("SUCCESS")


main()
