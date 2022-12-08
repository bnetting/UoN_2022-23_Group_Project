'''
Python Webscraper from live website
Webpage to scrape: https://nvd.nist.gov/
Libraries needed "pip install <>"
- beautifulsoup4
- lxml
- html5lib
- requests

Author - Anderson Jolly

'''

from bs4 import BeautifulSoup
import requests

htmlPage = requests.get('https://nvd.nist.gov/')  # URL to scrape
print(htmlPage)  # request 200 means successful request
htmlText = htmlPage.text
soup = BeautifulSoup(htmlText, 'lxml')  # allows pretty print with lxml parser

threats = soup.find_all('div', id='latestVulnsArea')
for i in threats:
    threat = i.find('ul', id='latestVulns')  # each whole row
    text = threat.find_all('div', class_="col-lg-9")
    for j in text:
        ID = j.find('strong').a.text  # id of the threat
        link = j.find('a', href=True)  # link to more information
        info = j.text  # text data
        text = info.split()  # array of text
        threatInfo = []
        date = []
        for word in range(0, len(text)):
            if text[word] == "-":
                threatInfo = text[word:]
            if text[word] == "read":
                date = text[word:]

        print(f'''ID:
{ID}
LINK:
{link}''')
        print("THREAT:")
        for item in threatInfo:
            print(item, end=" ")
        print("\nDATE:")
        for item in date:
            print(item, end=" ")
        print("\n#########################\n")



