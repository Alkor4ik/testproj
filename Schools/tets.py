
import requests
from bs4 import BeautifulSoup 
a = 'a'
print(a)

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
