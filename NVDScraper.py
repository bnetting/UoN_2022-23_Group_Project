"""
Python Webscraper
Webpage to scrape: https://services.nvd.nist.gov/rest/json/cves/2.0
Libraries needed "pip install <>"
- requests

Author - Anderson Jolly
"""

import json
import requests

url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
r = requests.get(url)

data = json.loads(r.text)
for item in data:
    print(item)
print(data['vulnerabilities'][0])
vulnerabilities = data['vulnerabilities']

for item in vulnerabilities:
    try:
        CVE_ID = item['cve']['id']
    except:
        CVE_ID = ""
        print("MISSING CVE")

    try:

        CVE_DESC = item['cve']['descriptions'][0]['value']
    except:
        CVE_DESC = ""
        print("MISSING CVE")

    try:
        CVE_DATE = item['cve']['lastModified']
    except:
        CVE_DATE = ""
        print("MISSING CVE")
    try:
        CVE_SEVERITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
    except:
        CVE_SEVERITY_SCORE = ""
        print("MISSING CVE")
    try:
        CVE_SEVERITY = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseSeverity']
    except:
        CVE_SEVERITY = ""
        print("MISSING CVE")
    try:
        CVE_TYPE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['accessVector']
    except:
        CVE_TYPE = ""
        print("MISSING CVE")
    try:
        CVE_LINK = item['cve']['references'][0]['url']
    except:
        CVE_LINK = ""
        print("MISSING CVE")

    print(CVE_ID)
    print(CVE_TYPE)
    print(CVE_DESC)
    print(CVE_DATE)
    print(CVE_SEVERITY_SCORE)
    print(CVE_SEVERITY)
    print(CVE_LINK)

