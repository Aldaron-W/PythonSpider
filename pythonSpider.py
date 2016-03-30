#!/usr/bin/python

from WebSpider import WebSpider

url="http://www.cili009.com"

webspider = WebSpider()
content = webspider.open_url(url)

print content
