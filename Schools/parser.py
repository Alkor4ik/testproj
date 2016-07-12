

import requests
from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text


def parse_schools(html, base):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find('div', class_='search-results').find_all('h2', class_='search-results-title')

    return ({'scholl_name': i.a.text, 'location': 'Moscow', 'url': str(base + i.a.get('href'))} for i in articles)

def parse_info(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    address = soup.find('ul', class_='col-sm-6 list-unstyled')
    address = address.find_next('ul', class_='col-sm-6 list-unstyled')

    # for i in info:
    #     print(i.text)

    return address.li.text.strip()


def main():
    URL = 'http://www.ucheba.ru/for-kids/schools'
    base = 'http://www.ucheba.ru'

    text = get_html(URL)
    schools = parse_schools(text, base)
    
    # any(print(s) for s in schools)
    for i in schools:
        # print(i['url'])
        print(parse_info(i['url']))



if __name__ == '__main__':
    main()