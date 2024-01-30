import requests
from bs4 import BeautifulSoup


def check_url(url):
    if 'nature.com/articles/' in url:
        return True
    else:
        return False


def main():
    url = input('Input the URL:\n')
    if check_url(url):
        response = requests.get(
            url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').get_text()
        description = soup.find_all('meta', {'name': 'description'})
        results = {'title': title, 'description': description[0]["content"]}
        print(results)
    else:
        print('Invalid page!')


if __name__ == '__main__':
    main()