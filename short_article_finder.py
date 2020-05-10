#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from preview import getNextPos, getLinks
from pool import Pool
from checker import check
import yaml
from telegram.ext import Updater
from existing import Existing
import os

existing = Existing()

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True) # translate bot, adhoc use
debug_group = tele.bot.get_chat(420074357)

pool = Pool()

while pool.pool:
	for name, pos in pool.items():
		for link in getLinks(name, pos):
			if check(link):
				print(link)
				if not existing.add(link):
					continue
				os.system('open %s -g' % link)
				# post = link
				# if len(link) > 20:
				# 	post = '[link](%s)' % link
				# debug_group.send_message(post, parse_mode='Markdown')
		next_pos = getNextPos(name, pos)
		pool.update(name, next_pos)