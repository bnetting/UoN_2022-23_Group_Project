'''
Python Webscraper
Webpage to scrape http://books.toscrape.com/
Libraries needed "pip install <>"
- beautifulsoup4
- lxml
- html5lib

Author - Anderson Jolly

'''
from bs4 import BeautifulSoup

with open('Sandbox.html', 'r') as htmlFile:
    content = htmlFile.read()
    print(content)
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())  # pretty print of the html
    h3Tags = soup.find_all('h3')  # finds tags in the html
    print(h3Tags)
    for tag in h3Tags:  # loops through the list of h3 tags and prints out the text
        print(tag.text)
