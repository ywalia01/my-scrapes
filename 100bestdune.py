from bs4 import BeautifulSoup
import requests

quotesList = []
file = open('bookriot_dune100bestquotes.txt', "w")

source = requests.get('https://bookriot.com/best-dune-quotes/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

for quote in soup.find_all('p'):
    quotesList.append(quote.text)
    # print(quote.text)

for x in range(len(quotesList)):
    print(quotesList[x])
    file.write(quotesList[x] + "\n")

file.flush()
file.close()
