#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from preview import getSlides, getUrls
import yaml
from telegram.ext import Updater
from existing import Existing
import os
import sys
import album_sender
from telegram_url import AlbumResult as Result

existing = Existing()

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True) # translate bot, adhoc use
debug_group = tele.bot.get_chat(420074357)
channel = tele.bot.get_chat('@web_record')

for url in getUrls():
	if existing.contain(url):
		continue
	r = Result()
	r.imgs = list(getSlides(url))
	
	if 'test' not in sys.argv:
		existing.add(url)

