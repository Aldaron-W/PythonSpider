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

    def get_shows(self, content):
        soup = bs4.BeautifulSoup(content, "lxml")
        div=soup.findAll('span', class_='b')               # return the first "div" tag
        #films_list = div.findAll('dl', class_="list-item")  # return the list of "li" tag under "div"
        return div

    def get_show_detail(self, shows_list):
        shows_detail = []

        for show in shows_list:
            # For each film
            show_dic = {}
            # retrieve corresponding informations
            show_dic['show_name'] = show.a.text
            # add all the informations of a film into list "films_sorted"
            shows_detail.append(show_dic)

        return shows_detail

    def regex_show_name(self, shows_detail):
        for show in shows_detail:
            show_detail = show['show_name'].split('.')
            pattern = re.compile(u'[\u4e00-\u9fa5]+')
            match = pattern.search(show_detail[0])

            if match:
                print show_detail[0]
                pass
        pass
    pass
