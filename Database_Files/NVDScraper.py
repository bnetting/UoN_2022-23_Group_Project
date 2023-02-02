"""
Python Webscraper
Webpage to scrape: https://services.nvd.nist.gov/rest/json/cves/2.0
Libraries needed "pip install <>"
- requests
- pandas
- xlsxwriter
- xlrd
- openpyxl
- thread

Author - Anderson Jolly
"""
import threading
import time

import numpy as np
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from threading import Thread
import threading

writer = pd.ExcelWriter('threats.xlsx', engine='xlsxwriter')
THREATS_PER_PAGE = 2000
NUMBER_OF_THREADS = 5
NUMBER_OF_CATEGORY_THREADS = 64
scraperThreads = []
categoryThreads = []
# these arrays are to create the dictionary of data for each vulnerability
ID = []
idLock = threading.Lock()
DESC = []
descLock = threading.Lock()
DATE = []
dateLock = threading.Lock()
TYPE = []
typeLock = threading.Lock()
CATEGORY = [None] * (THREATS_PER_PAGE * NUMBER_OF_THREADS)
catLock = threading.Lock()
SEVERITY = []
severityLock = threading.Lock()
SCORE = []
scoreLock = threading.Lock()
EXPLOITABILITY = []
exploitLock = threading.Lock()
IMPACT = []
impactLock = threading.Lock()
LINK1 = []
link1Lock = threading.Lock()
LINK2 = []
link2Lock = threading.Lock()

categoryID = []
catIDLock = threading.Lock()


def addCell(data, array, lock):
    lock.acquire()
    array.append(data)
    lock.release()


def addCellIndex(data, array, lock, id):
    idLock.acquire()
    index = ID.index(id)
    # print("---- ", ID[index])
    lock.acquire()
    array[index] = data
    # print("ADDED in Place", str(index))
    lock.release()
    idLock.release()


# This function will get the threat data when given a URL
def getData(url):
    r = requests.get(url)
    # gets data into JSON
    data = json.loads(r.text)
    # gets vulnerability col from JSON
    vulnerabilities = data['vulnerabilities']
    # DATA FOR EACH THREAT
    # for item in vulnerabilities:
    for i in range(0, THREATS_PER_PAGE):
        item = vulnerabilities[i]
        try:  # ID
            CVE_ID = item['cve']['id']
            addCell(CVE_ID, ID, idLock)
        except:
            CVE_ID = ""
            addCell(CVE_ID, ID, idLock)
            # print("MISSING ID")
        try:  # Description
            CVE_DESC = item['cve']['descriptions'][0]['value']
            addCell(CVE_DESC, DESC, descLock)
        except:
            CVE_DESC = np.nan
            # print("MISSING DESC")
            addCell(CVE_DESC, DESC, descLock)

        try:  # Date
            CVE_DATE = item['cve']['lastModified']
            DateString=str(CVE_DATE) #Converts CVE_DATE to a string
            Date_filtered=DateString[:DateString.index("T")] #Removes the time portion from the date 
            print(Date_filtered)
            addCell(Date_filtered, DATE, dateLock)

        except:
            CVE_DATE = np.nan
            addCell(CVE_DATE, DATE, dateLock)

        try:  # Threat level
            CVE_SEVERITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
            addCell(CVE_SEVERITY_SCORE, SCORE, severityLock)

        except:
            CVE_SEVERITY_SCORE = np.nan
            addCell(CVE_SEVERITY_SCORE, SCORE, severityLock)

        try:  # Severity score
            CVE_SEVERITY = item['cve']['metrics']['cvssMetricV2'][0]['baseSeverity']
            addCell(CVE_SEVERITY, SEVERITY, scoreLock)

        except:
            CVE_SEVERITY = np.nan
            addCell(CVE_SEVERITY, SEVERITY, scoreLock)

        try:  # Threat type
            CVE_TYPE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['accessVector']
            addCell(CVE_TYPE, TYPE, typeLock)

        except:
            CVE_TYPE = np.nan
            addCell(CVE_TYPE, TYPE, typeLock)

        try:  # Exploitability
            CVE_EXPLOITABILITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['exploitabilityScore']
            addCell(CVE_EXPLOITABILITY_SCORE, EXPLOITABILITY, exploitLock)

        except:
            CVE_EXPLOITABILITY_SCORE = np.nan
            addCell(CVE_EXPLOITABILITY_SCORE, EXPLOITABILITY, exploitLock)

        try:  # Impact
            CVE_IMPACT_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['impactScore']
            addCell(CVE_IMPACT_SCORE, IMPACT, impactLock)
        except:
            CVE_IMPACT_SCORE = np.nan
            addCell(CVE_IMPACT_SCORE, IMPACT, impactLock)

        try:  # Link 1
            CVE_LINK = item['cve']['references'][0]['url']
            addCell(CVE_LINK, LINK1, link1Lock)

        except:
            CVE_LINK = np.nan
            addCell(CVE_LINK, LINK1, link1Lock)

        try:  # Link 2
            CVE_LINK_2 = 'https://www.cvedetails.com/cve/' + CVE_ID + '/'
            addCell(CVE_LINK_2, LINK2, link2Lock)
        except:
            CVE_LINK_2 = ''
            addCell(CVE_LINK_2, LINK2, link2Lock)


# This function writes the data frame to the Excel spreadsheet
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
    # print(df)
    df = df.dropna()

    df.to_excel(writer, index=True, header=True)
    writer.close()
    print("WRITE SUCCESS")


# Function to get the total number of vulnerabilities from the NVD
def getTotal():
    r = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
    data = json.loads(r.text)
    return data['totalResults']


# Function to query the CVE website to extract the sub-type of category
# TODO need to be threaded
def getCategory(IDs, threadNo):
    threat_names = ['Denial Of Service', 'Execute Code', 'Overflow', 'Memory corruption',
                    'Sql Injection',
                    'Cross Site Scripting', 'Directory Traversal', 'Http response splitting',
                    'Bypass a restriction or similar',
                    'Obtain Information', 'Gain privileges', 'CSRF', 'File Inclusion']
    # pop
    while True:

        catIDLock.acquire()
        cve = IDs.pop(0)
        # print(cve)
        print("Thread", str(threadNo), " - " + str(len(IDs)))
        catIDLock.release()

        if cve:
            link = 'https://www.cvedetails.com/cve/' + cve + '/'
            r = requests.get(link)
            htmlText = r.text  # raw html text
            soup = BeautifulSoup(htmlText, 'lxml')
            try:
                category = soup.findAll('span')
                subCategory = category[21].text
                #  print("index = " + str(index) + " Cat = " + subCategory, "CVE = " + str(url) + "\n")
                if subCategory == "-" or subCategory == " ":
                    # print("found fuck all at " + str(cve) + "index " + str(ID.index(cve)))
                    addCellIndex(np.nan, CATEGORY, catLock, cve)
                else:
                    addCellIndex(subCategory, CATEGORY, catLock, cve)
            except:
                print("THREAD " + str(threadNo) + " SLEEPING")
        if len(IDs) == 0:
            False
            break
            #  addCellIndex(np.nan, CATEGORY, catLock, cve)

            subCategory = ""
            # addCellIndex(subCategory, CATEGORY, catLock, url)
        # catIDLock.release()


# idLock.release()

if __name__ == '__main__':

    for i in range(0, NUMBER_OF_THREADS):
        print("THREAD CREATION THREATS\n", str(i) + "\n")
        url = "https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex=" + str(i * 2000)
        print(url)
        t = threading.Thread(target=getData, args=(url,))
        scraperThreads.append(t)

    for i in range(0, NUMBER_OF_THREADS):
        scraperThreads[i].start()
        time.sleep(1)

    for i in range(0, NUMBER_OF_THREADS):
        scraperThreads[i].join()

    IDs = ID.copy()
    for x in range(0, len(ID)):
        print(ID[x])
    print(len(IDs), " LENGTH")

    for i in range(0, NUMBER_OF_CATEGORY_THREADS):
        t = threading.Thread(target=getCategory, args=(IDs, i))
        categoryThreads.append(t)

    for i in range(0, NUMBER_OF_CATEGORY_THREADS):
        categoryThreads[i].start()

    for i in range(0, NUMBER_OF_CATEGORY_THREADS):
        categoryThreads[i].join()
    print("Writing")

    print(len(ID))
    print(len(TYPE))
    print(len(SEVERITY))
    print(len(SCORE))
    print(len(EXPLOITABILITY))
    print(len(IMPACT))
    print(len(LINK1))
    print(len(DATE))
    print(len(LINK1))
    print(len(LINK2))
    print(len(CATEGORY))
    writeData()
