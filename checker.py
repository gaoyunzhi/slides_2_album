import readee
import cached_url
from telegram_util import cnWordCount

def check(link):
	try:
		content = cached_url.get(link, force_cache = True)
	except:
		return False
	soup = readee.export(link, content = content)
	if 200 < cnWordCount(soup.text) < 2500:
		return True
	return False
