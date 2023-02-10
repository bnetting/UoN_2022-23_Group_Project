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

df = pd.read_excel('threats.xlsx', engine='openpyxl', index_col=0)

NETWORK = 0
LOCAL = 1

LOW = 0
MEDIUM = 1
HIGH = 2

EXECUTE_CODE = 0
OVERFLOW = 1
GAIN_PRIVILEGES = 2
BYPASS_A_RESTRICTION_OR_SIMILAR = 3
DENIAL_OF_SERVICE = 4
CSRF = 5
FILE_INCLUSION = 6
CROSS_SITE_SCRIPTING = 7
SQL_INJECTION = 8
OBTAIN_INFORMATION = 9
DIRECTORY_TRAVERSAL = 10
HTTP_RESPONSE_SPLITTING = 11


def getMapping(string: str):  # Function to map string to an integer
    if string == 'NETWORK':
        return NETWORK
    elif string == 'LOCAL':
        return LOCAL
    elif string == 'LOW':
        return LOW
    elif string == 'MEDIUM':
        return MEDIUM
    elif string == 'HIGH':
        return HIGH
    elif string == 'Execute Code':
        return EXECUTE_CODE
    elif string == 'Overflow':
        return OVERFLOW
    elif string == 'Gain privileges':
        return GAIN_PRIVILEGES
    elif string == 'Bypass a restriction or similar':
        return BYPASS_A_RESTRICTION_OR_SIMILAR
    elif string == 'CSRF':
        return CSRF
    elif string == 'File Inclusion':
        return FILE_INCLUSION
    elif string == 'CSRF':
        return CSRF
    elif string == 'Cross Site Scripting':
        return CROSS_SITE_SCRIPTING
    elif string == 'Sql Injection':
        return SQL_INJECTION
    elif string == 'Obtain Information':
        return OBTAIN_INFORMATION
    elif string == 'Directory traversal':
        return FILE_INCLUSION
    elif string == 'Http response splitting':
        return HTTP_RESPONSE_SPLITTING
    else:
        return -1


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
        writer = pd.ExcelWriter('Database_files/threats.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=True, header=True)
        writer.close()
        print("WRITE SUCCESS")

        print("SUCCESS")

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
    test = str(round(temp, 2))
    return test


def getModalFromCol(column: str):  # Most common metric from a column
    temp = df[column].mode()[0]
    return str(temp)


def getCountFromCol(column: str, value: str):
    temp = df[column]
    count = temp.loc[temp == value].count()
    return count


# DATA FROM THREAT TYPES
def getAverageMetricFromCat(column: str, category: str):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mean()
    meanFinal = str(round(mean, 2))
    return meanFinal


def getModalMetricFromCat(column: str, category: int):  # Average metric per category
    temp = df.loc[df['CATEGORY'] == category]
    mean = temp[column].mode()
    return mean


def getCountFromCat(category: str):
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
    # TESTS FOR EXAMPLE USAGE
    print(getAverageMetricFromCol("IMPACT"))  # gets the average impact of all threats
    print(getAverageMetricFromCat("SCORE", 'Overflow'))  # gets the average score of an overflow threat
    print(getModalFromCol("CATEGORY"))  # gets the most common category of threat
    print(getCountFromCat('Overflow'))  # gets the number of overflow threats
    print(getThreatTypes())  # prints the list of all threats
    print(getModalFromCol("TYPE"))  # gets the most common type of threat
    print(getCountFromCol('TYPE', 'LOCAL'))  # gives the number of local threats


main()
