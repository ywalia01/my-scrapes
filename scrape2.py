from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.text
    # print(headline)

    summary = article.find('div', class_='entry-content').p.text
    # print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = f'https://www.youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    print(yt_link)
