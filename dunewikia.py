from bs4 import BeautifulSoup
import requests

x = 1
quotesList = []
source = requests.get(
    'https://en.wikipedia.org/wiki/List_of_Dune_characters').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

for quotes in soup.find_all('li'):
    quotesList.append(quotes)
    print(quotes.text)

# for x in range(len(quotesList)):
