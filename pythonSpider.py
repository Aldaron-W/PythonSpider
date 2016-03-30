#!/usr/bin/python
# encoding: utf-8

from WebSpider import WebSpider

url="http://cili009.com"

webspider = WebSpider()
content = webspider.open_url(url)
shows = webspider.get_shows(content)
detail = webspider.get_show_detail(shows)

print detail
