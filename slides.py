#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from preview import getUrls, getImgs
import yaml
from telegram.ext import Updater
from telegram import InputMediaPhoto
from existing import Existing
import os
import sys
import album_sender
from telegram_util import AlbumResult as Result
import pic_cut

existing = Existing()

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True) # translate bot, adhoc use
debug_group = tele.bot.get_chat(420074357)
channel = tele.bot.get_chat('@web_record')

def send(chat, imgs):
	group = []
	for img in imgs:
		fn = pic_cut.getCutImages([img['data-lazy']], 1)[0]
		group.append(InputMediaPhoto(open(fn, 'rb'), caption=img['alt']))
		if len(group) == 9:
			break
	chat.bot.send_media_group(chat.id, group)

for url in getUrls():
	if existing.contain(url):
		continue
	send(debug_group, getImgs(url))
	if 'test' not in sys.argv:
		existing.add(url)
	break # testing

