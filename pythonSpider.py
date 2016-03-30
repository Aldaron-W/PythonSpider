#!/usr/bin/python
# coding: utf-8

from WebSpider import WebSpider

url="http://cili009.com"

webspider = WebSpider()
content = webspider.open_url(url)
shows = webspider.get_shows(content)
detail = webspider.get_show_detail(shows)
webspider.regex_show_name(detail)

# for show in detail:
# 	print (show['show_name'].split('.'))
