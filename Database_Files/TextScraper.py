'''
Python Webscraper for prices
Webpage to scrape http://books.toscrape.com/
Libraries needed "pip install <>"
- beautifulsoup4
- lxml
- html5lib

Author - Anderson Jolly

'''
from bs4 import BeautifulSoup
titles = []
cost = []

with open('Sandbox.html', 'r') as htmlFile:
    content = htmlFile.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())  # pretty print of the html
    names = soup.find_all('h3')
    for title in names:
        title.find("title")
        name = title.a.text
        print(name)
        titles.append(name)

    prices = soup.findAll('div', class_='product_price')
    for product in prices:
        price = product.p.text.replace("Â","")  # removed char in the statement
        cost.append(price)

    print(dict(zip(titles, cost)))


