#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from preview import getSlides, getUrls, getCaption, getImgs
import yaml
from telegram.ext import Updater, InputMediaPhoto
from existing import Existing
import os
import sys
import album_sender
from telegram_util import AlbumResult as Result

existing = Existing()

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True) # translate bot, adhoc use
debug_group = tele.bot.get_chat(420074357)
channel = tele.bot.get_chat('@web_record')

def send(imgs, url):
	group = []
	for img in imgs:
		cap = img['alt'] + '[source](%s)' % url
		group.append([InputMediaPhoto(img['data-lazy'],
			caption=cap, parse_mode='Markdown')])
		if len(group) == 9:
			break
	chat.bot.send_media_group(debug_group.id, group)

for url in getUrls():
	if existing.contain(url):
		continue
	send(getImgs(url), url)
	if 'test' not in sys.argv:
		existing.add(url)
	return # testing

