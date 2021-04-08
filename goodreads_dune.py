from bs4 import BeautifulSoup
import requests

file = open('parsed_data.txt', "w")
x = 1
quotesList = []
for x in range(26):
    source = requests.get(
        'https://www.goodreads.com/work/quotes/3634639-dune?page=' + str(x)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    for quotes in soup.find_all('div', class_='quoteText'):
        quotesList.append(quotes.text)
        # print(quotes.text)

for x in range(len(quotesList)):
    file.write(quotesList[x])

file.flush()
file.close()
