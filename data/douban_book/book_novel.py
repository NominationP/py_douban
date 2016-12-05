#!/usr/bin/env python
# coding:utf8

'''

function : find detail message of each novel book by url_novel to book_navel.txt
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

import socket

socket.setdefaulttimeout(3)
f = open("proxy.txt")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("^")
    proxy_host = ip[0]+":"+ip[1]
    # proxy_temp = {"http":proxy_host}
    proxys.append(proxy_host)

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



def find_each_type_detatil(read_file,write_file,log_file) :


    fw_log = open(log_file,'aw')

    detail_one = []

    current_tag =read_file.split("_")[3]
    num_lines = sum(1 for line in open(read_file))

    fr = open(read_file, 'r')
    fw = open(write_file, 'w')

    fw.write('title^author^pub^date^pages^price^binding^ISBN^rate^vote'+'\n')
    col = ['出版社:','出版年:','页数:','定价:','装帧:','ISBN:']


    firstLine = True

    num = 0

    print '******************************'
    print current_tag
    print '******************************'

    for line in fr:
        # print "dddddddddddddd"
        # if num <= 5 :
        #     continue

        # if num == 5 :
        #     break

        # if firstLine:
        #     firstLine = False
        #     continue


        # set time sleep
        # time.sleep(0.500)

        # get
        request = urllib2.Request(url=line,headers=hdr)




        for proxy in proxys:
            try:
                proxy_temp = urllib2.ProxyHandler({'https': proxy})
                opener = urllib2.build_opener(proxy_temp)
                urllib2.install_opener(opener)
                response = urllib2.urlopen(request, timeout=20)
                break
            except Exception,e:
                print e
                continue
            break



        result = response.read()
        result = BeautifulSoup(result)

        title = result.h1.get_text().strip()
        rrr = result.find_all('div',{'class':'subjectwrap'})[0].find_all('span')

        num += 1
        print num,
        if(num == int(num_lines/4)):
            print (time.strftime("%H:%M:%S")+"20%"+" "+str(num) +" "+ title.encode('utf8')+" "+line.strip('\n'))
        if(num == int(num_lines/2)):
            print (time.strftime("%H:%M:%S")+"50%"+" "+str(num) +" "+ title.encode('utf8')+" "+line.strip('\n'))
        if(num == int(num_lines-num_lines/4)):
            print (time.strftime("%H:%M:%S")+"80%"+" "+str(num) +" "+ title.encode('utf8')+" "+line.strip('\n'))
        if num == num_lines:
            print (time.strftime("%H:%M:%S")+"100%"+" "+str(num) +" "+ title.encode('utf8')+" "+line.strip('\n'))

        count = 0
        detail_one = []
        detail_col = []
        for x in rrr:
            if count == 0 or count == 1:
                if count == 0 :
                    author = rrr[0].a.get_text()
                count += 1
                continue
            if x.get_text() in col :

                sibling =  x.next_sibling

                if '+' in str(sibling) :
                    sibling = x.next_sibling.split("+")[0]
                    print "+++"+str(sibling)+" "+line

                detail_one.append(sibling.strip())
                detail_col.append(x.get_text().strip().encode('utf8'))


        # print "detail_col : " + str(detail_col)
        # some message not pages !!!! fuck!
        aa = set(col)
        bb = set(detail_col)

        diff = list(aa.difference(bb))

        # print len(diff)

        if len(diff) != 0:

            for x in diff:
                index =col.index(x)
                detail_one.insert(index,str(0))

        count += 1



        # get rate and vote count
        rate = result.find_all('div',{'class':'subjectwrap'})[0].find_all("strong")[0].get_text().strip()

        if rate == "":
            rate = str(0)
            vote = str(0)
        else :
            vote = (result.find_all('div',{'class':'subjectwrap'})[0]).find_all('span',{'property':'v:votes'})[0].get_text().strip()

        record = str(title.encode('utf8')+'^'+author.encode('utf8')+'^'+detail_one[0]+'^'+detail_one[1]+'^'+detail_one[2]+'^'+detail_one[3].split("元")[0]+'^'+detail_one[4]+'^'+detail_one[5]+'^'+rate+'^'+vote+'\n')

        fw.write(record)

    line_new = '{:>10}  {:>10}  {:>10}'.format(current_tag, num_lines, time.strftime("%Y/%m/%d %H:%M:%S"))
    fw_log.write(line_new+'\n')
    fw_log.close()
    fw.close()
    fr.close()

    # print result.find_all('div',{'class':'ckdPopularBooks'})[0].find_all('h4',class_ =['title'])[0].get_text()



fix_add = '/home/git/fullstack-data-engineer/data/douban_book/url'

read_all_file = (   fix_add+'/url_Culture/url_Culture_book_sim.txt',
                    fix_add+'/url_Life/url_Life_book_sim.txt',
                    fix_add+'/url_Literature/url_Literature_book_sim.txt',
                    fix_add+'/url_Management/url_Management_book_sim.txt',
                    fix_add+'/url_Popular/url_Popular_book_sim.txt',
                    fix_add+'/url_Science/url_Science_book_sim.txt')

write_all_file = (  fix_add+'/url_Culture/url_Culture_book_detail.txt',
                    fix_add+'/url_Life/url_Life_book_detail.txt',
                    fix_add+'/url_Literature/url_Literature_book_detail.txt',
                    fix_add+'/url_Management/url_Management_book_detail.txt',
                    fix_add+'/url_Popular/url_Popular_book_detail.txt',
                    fix_add+'/url_Science/url_Science_book_detail.txt')

# for x in xrange(0,5):
find_each_type_detatil(read_all_file[0],write_all_file[0],'all_book_detail_log.txt')
