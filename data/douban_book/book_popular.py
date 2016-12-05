#!/usr/bin/env python
# coding:utf8


'''

function : find 最受关注图书榜 (20) to popular.txt
author   : Zhangze
date     : 2016-12-02

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup

urlX = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
urlI = 'https://book.douban.com/chart?subcat=I'
urlF = 'https://book.douban.com/chart?subcat=F'

urlsum = [urlI,urlF]

# all book url
urlarray=[]
# one book detail
detail_all = []
detail_one = []

for url in urlsum :
    # get
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    result = BeautifulSoup(result)

    result = result.find_all('ul',class_=["chart-dashed-list"])[0].find_all('li')

    for x in xrange(0,len(result)):
        urlarray.append(result[x].a['href'])

fw = open('book_popular.txt', 'w')
fw.write('title^author^pub^date^pages^price^binding^ISBN^rate^vote'+'\n')
col = ['出版社:','出版年:','页数:','定价:','装帧:','ISBN:']






for url in xrange(0,len(urlarray)):

    detail_one = []

    # get
    request = urllib2.Request(url=urlarray[url])
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    result = BeautifulSoup(result)

    title = result.h1.get_text().strip()
    rrr = result.find_all('div',{'class':'subjectwrap'})[0].find_all('span')
    print url

    count = 0
    for x in rrr:
        if count == 0 or count == 1:
            if count == 0 :
                author = rrr[0].a.get_text()
            count += 1
            continue
        if x.get_text() in col :
            detail_one.append(x.next_sibling.strip())
        count += 1



    # get rate and vote count
    rate = result.find_all('div',{'class':'subjectwrap'})[0].find_all("strong")[0].get_text().strip()
    vote = (result.find_all('div',{'class':'subjectwrap'})[0]).find_all('span',{'property':'v:votes'})[0].get_text().strip()


    record = str(title.encode('utf8')+'^'+author.encode('utf8')+'^'+detail_one[0]+'^'+detail_one[1]+'^'+detail_one[2]+'^'+detail_one[3].split("元")[0]+'^'+detail_one[4]+'^'+detail_one[5]+'^'+rate+'^'+vote+'\n')

    fw.write(record)


fw.close()
# print result.find_all('div',{'class':'ckdPopularBooks'})[0].find_all('h4',class_ =['title'])[0].get_text()

