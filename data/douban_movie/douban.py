#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'

# get
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read());
tags = result['tags']

movies = []


for tag in tags:
  limit = 0
  while 1:
    url ='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&sort=recommend&page_limit=20&page_start='+str(limit)
    # get
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = json.loads(response.read());
    result = result['subjects']

    if len(result) == 0 :
      break

    limit += 20
    for item in result :
      movies.append(item)

    #####
    break
  #####
  break

for x in xrange(0,len(movies)):
  itme = movies[x]
  # get
  request = urllib2.Request(url=itme['url'])
  response = urllib2.urlopen(request, timeout=20)
  result = response.read();

  html = BeautifulSoup(result)
  title = html.select('h1')[0]
  title = title.select('span')[0]
  title = title.get_text()

  print movies[x]['title']

  movies[x]['title'] = title

fw = open('movies.txt', 'w')

for item in movies:
  tmp = ''
  for key,value in item.items():
    tmp += str(value) + ','
  fw.write(tmp[:-1] + '\n')

fw.close()

# fw = open('movies.txt', 'w')

# for x in xrange(0,len(movies)):
#   tmp = ''
#   # for key,value in item.items():
#   tmp += movies[x]['title'] + ',' + str(movies[x]['rate'])
#   fw.write(tmp[:-1] + '\n')

# fw.close()






