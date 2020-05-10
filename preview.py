from bs4 import BeautifulSoup
import cached_url

DOMAIN = 'https://cn.reuters.com'

def getUrls():
	root = DOMAIN + '/news/archive/specialEvents27'
	b = BeautifulSoup(cached_url.get(root), 'html.parser')
	for item in b.find_all('div', class_='story-content'):
		yield item.find('a')['href']

def getSlides(url):
	b = BeautifulSoup(cached_url.get(DOMAIN + url, force_cache=True), 'html.parser')
	for item in b.find_all('div', class_='slide-image-enclosure'):
		img = item.find('img')
		yield img['data-lazy']
		img['alt'] # todo add caption


