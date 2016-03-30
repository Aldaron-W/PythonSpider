#!/usr/bin/python

from WebSpider import WebSpider

url="http://cili009.com"

webspider = WebSpider()
content = webspider.open_url(url)
shows = webspider.get_shows(content)

print shows
