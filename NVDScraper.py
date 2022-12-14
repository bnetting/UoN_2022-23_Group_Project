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

vulnerabilities = data['vulnerabilities']


for item in vulnerabilities:
    try:
        CVE_ID = item['cve']['id']
    except:
        CVE_ID = ""
        print("MISSING ID")
    try:
        CVE_DESC = item['cve']['descriptions'][0]['value']
    except:
        CVE_DESC = ""
        print("MISSING DESC")
    try:
        CVE_DATE = item['cve']['lastModified']
    except:
        CVE_DATE = ""
        print("MISSING DATE")
    try:
        CVE_SEVERITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
    except:
        CVE_SEVERITY_SCORE = ""
        print("MISSING SEVERITY SCORE")
    try:
        CVE_SEVERITY = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseSeverity']
    except:
        CVE_SEVERITY = ""
        print("MISSING SEVERITY")
    try:
        CVE_TYPE = item['cve']['metrics']['cvssMetricV2'][0]['cvssData']['accessVector']
    except:
        CVE_TYPE = ""
        print("MISSING CVE TYPE")
    try:
        CVE_LINK = item['cve']['references'][0]['url']
    except:
        CVE_LINK = ""
        print("MISSING CVE LINK")
    try:
        CVE_LINK_2 = item['cve']['references'][1]['url']
    except:
        CVE_LINK_2 = ""
        print("MISSING CVE LINK 2")
    try:
        CVE_EXPLOITABILITY_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['exploitabilityScore']
    except:
        CVE_EXPLOITABILITY_SCORE = ""
        print("MISSING CVE EXPLOITABILITY")
    try:
        CVE_IMPACT_SCORE = item['cve']['metrics']['cvssMetricV2'][0]['impactScore']
    except:
        CVE_IMPACT_SCORE = ""
        print("MISSING CVE IMPACT")

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

