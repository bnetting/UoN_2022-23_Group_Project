"""
Python Webscraper
Webpage to scrape: https://services.nvd.nist.gov/rest/json/cves/2.0
Libraries needed "pip install <>"
- requests
- pandas
- xlsxwriter
- xlrd
- openpyxl

Author - Anderson Jolly
"""
import time

import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

writer = pd.ExcelWriter('threats.xlsx', engine='xlsxwriter')

ID = []
DESC = []
DATE = []
TYPE = []
CATEGORY = []
SEVERITY = []
SCORE = []
EXPLOITABILITY = []
IMPACT = []
LINK1 = []
LINK2 = []


def getData(url):
    r = requests.get(url)
    # gets data into JSON
    data = json.loads(r.text)
    # gets vulnerability col from JSON
    vulnerabilities = data['vulnerabilities']
    # DATA FOR EACH THREAT
    # for item in vulnerabilities:
    for i in range(0, 10):
        item = vulnerabilities[i]
        # print(item)
        try:
            CVE_ID = item['cve']['id']
            ID.append(CVE_ID)
        except:
            CVE_ID = ""
            print("MISSING ID")
        try:
            CVE_DESC = item['cve']['descriptions'][0]['value']
            DESC.append(CVE_DESC)
        except:
            CVE_DESC = ""
            print("MISSING DESC")
            DESC.append(CVE_DESC)

        try:
            CVE_DATE = item['cve']['lastModified']
            DATE.append(CVE_DATE)
        except:
            CVE_DATE = ""
            print("MISSING DATE")
            DATE.append(CVE_DATE)

        try:
            CVE_SEVERITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
            SCORE.append(CVE_SEVERITY_SCORE)
        except:
            CVE_SEVERITY_SCORE = ""
            print("MISSING SEVERITY SCORE")
            SCORE.append(CVE_SEVERITY_SCORE)

        try:
            # print(item['cve']['metrics']['cvssMetricV2'][0]['baseSeverity'])
            CVE_SEVERITY = item['cve']['metrics']['cvssMetricV2'][0]['baseSeverity']
            SEVERITY.append(CVE_SEVERITY)
        except:
            CVE_SEVERITY = ""
            print("MISSING SEVERITY")
            SEVERITY.append(CVE_SEVERITY)

        try:
            CVE_TYPE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['accessVector']
            TYPE.append(CVE_TYPE)
        except:
            CVE_TYPE = ""
            print("MISSING CVE TYPE")
            TYPE.append(CVE_TYPE)

        try:
            CVE_LINK = item['cve']['references'][0]['url']
            LINK1.append(CVE_LINK)
        except:
            CVE_LINK = ""
            print("MISSING CVE LINK")
            LINK1.append(CVE_LINK)

        try:
            CVE_LINK_2 = item['cve']['references'][1]['url']
            LINK2.append(CVE_LINK_2)
        except:
            CVE_LINK_2 = ""
            print("MISSING CVE LINK 2")
            LINK2.append(CVE_LINK_2)

        try:
            CVE_EXPLOITABILITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['exploitabilityScore']
            EXPLOITABILITY.append(CVE_EXPLOITABILITY_SCORE)
        except:
            CVE_EXPLOITABILITY_SCORE = ""
            print("MISSING CVE EXPLOITABILITY")
            EXPLOITABILITY.append(CVE_EXPLOITABILITY_SCORE)

        try:
            CVE_IMPACT_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['impactScore']
            IMPACT.append(CVE_IMPACT_SCORE)
        except:
            CVE_IMPACT_SCORE = ""
            print("MISSING CVE IMPACT")
            IMPACT.append(CVE_IMPACT_SCORE)

        print(f"ID: {CVE_ID} \n"
              f"TYPE: {CVE_TYPE} \n"
              f"DESCRIPTION: {CVE_DESC} \n"
              f"DATE: {CVE_DATE} \n"
              f"THREAT LEVEL: {CVE_SEVERITY} \n"
              f"BASE SEVERITY: {CVE_SEVERITY_SCORE} \n"
              f"EXPLOITABILITY: {CVE_EXPLOITABILITY_SCORE} \n"
              f"IMPACT: {CVE_IMPACT_SCORE} \n"
              f"LINK: {CVE_LINK} \n"
              f"SECONDARY LINK: {CVE_LINK_2} \n")


def writeData():
    df = pd.DataFrame({'ID': ID,
                       'TYPE': TYPE,
                       'CATEGORY': CATEGORY,
                       'DESCRIPTION': DESC,
                       'SEVERITY': SEVERITY,
                       'SCORE': SCORE,
                       'EXPLOITABILITY': EXPLOITABILITY,
                       'IMPACT': IMPACT,
                       'DATE': DATE,
                       'LINK': LINK1,
                       'OTHER': LINK2})

    df = df.dropna()

    df.to_excel(writer, index=True, header=True)
    writer.close()


def getTotal():
    r = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
    data = json.loads(r.text)
    return data['totalResults']


def getCategory(url):
    threat_names = ['Denial Of Service', 'Execute Code', 'Overflow', 'Memory corruption',
                    'Sql Injection',
                    'Cross Site Scripting', 'Directory Traversal', 'Http response splitting',
                    'Bypass a restriction or similar',
                    'Obtain Information', 'Gain privileges', 'CSRF', 'File Inclusion']
    r = requests.get('https://www.cvedetails.com/cve/' + url + '/')
    htmlText = r.text  # raw html text
    soup = BeautifulSoup(htmlText, 'lxml')
    try:
        category = soup.findAll('span')
        subCategory = category[21].text
        print(subCategory)
        if subCategory == "-":
            CATEGORY.append("")
        else:
            CATEGORY.append(subCategory)
    except:
        CATEGORY.append("")


if __name__ == '__main__':
    # total = getTotal()
    # print(total)
    getData('https://services.nvd.nist.gov/rest/json/cves/2.0')
    '''for i in range(0, total, 2000):
        #print(i)
        getData('https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex='+str(i))
        time.sleep(10)'''
    print(len(ID))
    print(len(TYPE))
    print(len(SEVERITY))
    print(len(SCORE))
    print(len(EXPLOITABILITY))
    print(len(IMPACT))
    print(len(LINK1))
    print(len(DATE))
    print(len(LINK1))
    for x in ID:
        getCategory(x)

    writeData()
