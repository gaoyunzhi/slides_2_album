from bs4 import BeautifulSoup
import cached_url

DOMAIN = 'https://cn.reuters.com'

def getUrls():
	root = DOMAIN + '/news/archive/specialEvents27'
	b = BeautifulSoup(cached_url.get(root), 'html.parser')
	for item in b.find_all('div', class_='story-content'):
		yield DOMAIN + item.find('a')['href']

def getImgs(url):
	b = BeautifulSoup(cached_url.get(url, force_cache=True), 'html.parser')
	for item in b.find_all('div', class_='slide-image-enclosure'):
		yield item.find('img')

def getSlides(url):
	for img in getImgs(url):
		yield img['data-lazy']

def getCaption(url):
	for img in getImgs(url):
		yield img['alt']


