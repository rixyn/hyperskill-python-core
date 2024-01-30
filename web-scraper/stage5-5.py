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
import os
import requests
import string
from bs4 import BeautifulSoup

URL = 'https://www.nature.com/nature/articles'
BASE_URL = 'https://www.nature.com'


def parse_title(text):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in text if ch not in exclude).replace(
        "’", "").replace(" ", "_")
    return s + '.txt'


def save_file(page, title, body):
    folder = f"Page_{page}"
    file_name = folder + "/" + title
    if not os.path.isdir(folder):
        os.mkdir(folder)
    txt_file = open(file_name, 'wb')
    txt_file.write(body.encode())
    txt_file.close()

def create_folder(page):
    folder = f"Page_{page}"
    if not os.path.isdir(folder):
        os.mkdir(folder)

def article_body(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        article_text = soup.find(
            'div', {'class': 'c-article-body main-content'})
        return article_text.get_text().strip()
    except AttributeError:
        article_text = soup.find(
            'p', {'class': 'article__teaser'})
        return article_text.get_text().strip()


def main(pages, topic):
    for page in range(1, pages + 1):
        create_folder(page)
        params = {"sort": "PubDate", "year": "2020", "page": page}
        r = requests.get(URL, params=params)
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('article')
        if not articles:
            continue
        for article in articles:
            article_tag = article.find('span', {'data-test': 'article.type'})
            if article_tag.get_text().strip() == topic:
                link = article.find('a', {'data-track-action': 'view article'})
                title = link.get_text()
                link_url = link['href']
                full_url = BASE_URL + link_url
                clean_title = parse_title(title)
                save_file(page, clean_title, article_body(full_url))
        print(f'Saved articles on page {page}')


if __name__ == '__main__':
    pages = int(input("Insert total number of pages: "))
    topic = input("Insert topic: ")
    main(pages, topic)
'''