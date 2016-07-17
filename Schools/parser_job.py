import requests
from bs4 import BeautifulSoup



def get_html(URL):
	return requests.get(URL).text 

def parase_job(URL):
	html = get_html(URL)
	soup = BeautifulSoup(html, 'html.parser')
	articles = soup.find_all('div', class_='LandingPageListElement')
	jobes = []
	for i in articles:
		name_teacher = i.find('a', class_="h_visited_link LandingPageListElement_link vacancy-url").text.strip()
		school_name = i.find('div', class_="LandingPageListElement_company").text.strip()
		jobes.append({
			'name_teacher': name_teacher,
			'school_name': school_name
			})
	#articles = articles.prettify()
	print (jobes)


def main():
	URL = "http://www.superjob.ru/vakansii/uchitel.html"
	parase_job(URL)
	

if __name__ == '__main__':
	main()
