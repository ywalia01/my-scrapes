from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print("=============================")
# article = soup.find('div', class_='article')
# print(article)
# print("=============================")
# headline = article.h2.a.text
# print(headline)
# print("=============================")
# summary = article.p.text
# print(summary)
# print("=============================")

print("=============================")
for article in soup.find_all('div', class_='article'):
    print(article)
    print("=============================")
    headline = article.h2.a.text
    print(headline)
    print("=============================")
    summary = article.p.text
    print(summary)
    print("=============================")
