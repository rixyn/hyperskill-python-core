#source.html
'''
<html>
<head>
  <title>warming up</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="calc.jpg"><br>
<font color="gold">
<p>Hint: try to change the URL address.
</body>
</html>
'''

#scraper.py
'''
import requests
import string
from bs4 import BeautifulSoup

URL = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
BASE_URL = 'https://www.nature.com'


def parse_title(text):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in text if ch not in exclude).replace(
        "’", "").replace(" ", "_")
    return s + '.txt'


def save_file(title, body):
    txt_file = open(title, 'wb')
    txt_file.write(body.encode())
    txt_file.close()


def article_body(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    article_text = soup.find(
        'div', {'class': 'c-article-body main-content'})
    return article_text.get_text().strip()


def main():
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    url_list = []
    url_titles = []
    for article in soup.find_all('article'):
        article_tag = article.find('span', {'data-test': 'article.type'})
        if article_tag.get_text().strip() == 'News':
            link = article.find('a', {'data-track-action': 'view article'})
            title = link.get_text()
            link_url = link['href']
            full_url = BASE_URL + link_url
            clean_title = parse_title(title)
            url_titles.append(clean_title)
            url_list.append(full_url)
            save_file(clean_title, article_body(full_url))
    print('Saved articles: ' + str(url_titles))


if __name__ == '__main__':
    main()
'''