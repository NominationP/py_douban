#!/usr/bin/env python
# coding:utf8

'''

function : find all url to url
author   : Zhangze
date     : 2016-12-03

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import time

import json
from bs4 import BeautifulSoup

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

url_novel = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'



six_name = {"Literature":"文学","Popular":"流行","Culture":"文化","Life":"生活","Management":"经管","Science":"科技"}

for name in six_name:
  fr = open("/home/git/fullstack-data-engineer/data/douban_book/url/"+"url_"+str(name.encode('utf8'))+"/"+"url_"+str(name)+".txt", "r")

  print '*********************************'
  print name.encode('utf8')
  print '*********************************'

  for line in fr:
    url = 'https://book.douban.com/tag/'+line.strip()

    print line.strip()

    number = 0
    urlarray = []

    while number<=1200:
        # get
        request = urllib2.Request(url=url+"?start="+str(number)+'&type=T',headers=hdr)
        # print 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='+str(number)+'&type=T'
        while True:
            try:
                response = urllib2.urlopen(request, timeout=20)
            except :
                print "try"
                continue
            break
        result = response.read()
        result = BeautifulSoup(result)

        result = result.find_all('ul',class_=["subject-list"])[0]
        if result.get_text().strip() == "":
            break
        result = result.find_all('li')

        # print result

        for x in xrange(0,len(result)):
            if result[x].a['href'] not in urlarray:
                urlarray.append(result[x].a['href'])
        # if(number%500 == 0 and number!=0):
        #     print number

        number += 20

    fw = open("/home/git/fullstack-data-engineer/data/douban_book/url/"+"url_"+str(name.encode('utf8'))+"/"+"url_"+str(name)+"_book.txt", "aw")

    print len(urlarray)
    fw_log = open("url_log.txt",'aw')
    fw_log.write(name.encode('utf8')+" "+line.strip()+" "+str(len(urlarray))+"\t"+time.strftime("%Y-%m-%d %H:%M")+'\n')
    fw_log.close
    for x in urlarray :
        # print x
        fw.write(x+'\n')

    fw.close()