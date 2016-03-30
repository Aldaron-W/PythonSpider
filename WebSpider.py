#!/usr/bin/python
#coding: utf-8

import urllib2  # functions and classes which help in opening URLs
import bs4      # extract data from HTML or XML files
import chardet  # detect encoding character of HTML file
import re

class WebSpider:
    def __init__(self):
        self.__headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')

    def open_url(self, url):
        opener = urllib2.build_opener()           # create an OpenerDirector object
        opener.addheaders = [self.__headers]      # set HTTP headers
        content = opener.open(url).read()         # open the url and get the corresponding HTML contents
        encoding = chardet.detect(content)['encoding']  # changing character encoding
        content = content.decode(encoding, 'ignore')
        return content
