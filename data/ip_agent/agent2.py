#!/usr/bin/env python
# coding:utf8

'''

function : find all url_novel to url_novel.txt
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




# 作者：黄哥
# 链接：https://zhuanlan.zhihu.com/p/21638222
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# coding:utf-8

import requests
from bs4 import BeautifulSoup


class SpiderProxy(object):
    """黄哥Python培训 黄哥所写 Python版本为2.7以上"""
    headers = {
        "Host": "www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://www.xicidaili.com/wt/1",
    }

    def __init__(self, session_url):
        self.req = requests.session()
        self.req.get(session_url)

    def get_pagesource(self, url):
        html = self.req.get(url, headers=self.headers)
        return html.content

    def get_all_proxy(self, url, n):
        data = []
        for i in range(1, n):
            html = self.get_pagesource(url + str(i))
            soup = BeautifulSoup(html, "lxml")

            table = soup.find('table', id="ip_list")
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                tmp = []
                for item in cells:

                    tmp.append(item.find(text=True))
                data.append(tmp[1:3])
        return data


fw = open('proxy2.txt','aw')
session_url = 'http://www.xicidaili.com/wt/1'
url = 'http://www.xicidaili.com/wt/'
p = SpiderProxy(session_url)
proxy_ip = p.get_all_proxy(url, 10)
for item in proxy_ip:
    if item:
        fw.write(item[0]+"^"+item[1]+"\n")
        # fw.write(item+"\n")