#!/usr/bin/env python
# coding:utf8

'''

step     : 1

function : get all tags type and url of douban_book
author   : Zhangze
date     : 2016-12-03

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



request = urllib2.Request(url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all',headers=hdr)
# print 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='+str(number)+'&type=T'
response = urllib2.urlopen(request, timeout=20)
result = response.read()
result = BeautifulSoup(result)


six_name = {"文学":"Literature","流行":"Popular","文化":"Culture","生活":"Life","经管":"Management","科技":"Science"}


# get big seven_type
all_big_type = []
seven_type = result.find_all('h2')
for x in seven_type:
  all_big_type.append(x.get_text()[0:2])

alltag = []

result = result.find_all('table',class_=["tagCol"])

i = 0;

for big_type in result:
  file_name = "url_"+str(six_name[seven_type[i].get_text()[0:2].encode('utf8')])
  i += 1
  fw = open("/home/git/fullstack-data-engineer/data/douban_book/url/"+str(file_name)+"/"+str(file_name)+".txt", "w")
  for tag in big_type.find_all('a'):
    fw.write(tag.get_text().strip()+'\n')
  fw.close()
