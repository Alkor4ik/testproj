

import requests
from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text

def parse_info(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    address = soup.find('ul', class_='col-sm-6 list-unstyled')
    address = address.find_next('ul', class_='col-sm-6 list-unstyled')

    # for i in info:
    #     print(i.text)

    return address.li.text.strip()


def parse_schools(URL, base):
    html = get_html(URL)
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find('div', class_='search-results').find_all('h2', class_='search-results-title')
    schools = []
    for i in articles:
        school_url = str(base + i.a.get('href'))
        school_html = get_html(school_url)
        school_soup = BeautifulSoup(school_html, "html.parser") 
        address = school_soup.find('ul', class_='col-sm-6 list-unstyled')
        address = address.find_next('ul', class_='col-sm-6 list-unstyled')
        address = address.li.text.strip()
        schools.append({
            'url': school_url,
            'scholl_name': i.a.text,
            'location': address,
            })
    return schools
    #({'scholl_name': i.a.text, 'location': 'Moscow', 'url': str(base + i.a.get('href'))} for i in articles)

def parse_all_school(URL, base):
    html = get_html(URL)
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.find('div', class_='paginator mt-section')
    pagination = int(pagination.find_all('a')[-1].text)
    all_schools = []
    print ('Всего страниц со школами ' + str(pagination))
    file = open("parser.txt", 'a')
    for i in range(0,pagination*30,30):
        URL_page = str(URL+'?s='+str(i))
        print('Сейчас парсим '+ URL_page+' страницу')
        schools = parse_schools(URL_page, base)
        file.write(str(schools))
        all_schools = all_schools + schools
    file.close()
    return all_schools
    



def main():
    URL = 'http://www.ucheba.ru/for-kids/schools'
    base = 'http://www.ucheba.ru'

    #text = get_html(URL)
    #schools = parse_schools(URL, base)
    all_school = parse_all_school(URL, base)

    
    # any(print(s) for s in schools)
    #for i in schools:
        # print(i['url'])
    #    print (i)



if __name__ == '__main__':
    main()
