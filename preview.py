from bs4 import BeautifulSoup
import cached_url

def getSoup(name, pos):
	url = 'https://t.me/s/%s/%d' % (name, pos)
	content = cached_url.get(url, force_cache = True)
	return BeautifulSoup(content, 'html.parser')

def getNextPos(name, pos):
	soup = getSoup(name, pos)
	next_pos = pos
	for item in soup.find_all('div', class_='tgme_widget_message'):
		next_pos = int(item.get('data-post', '').split('/')[-1]) + 1
	return next_pos

def getLinks(name, pos):
	soup = getSoup(name, pos)
	for item in soup.find_all('a', class_='tgme_widget_message_link_preview'):
		yield item['href']

