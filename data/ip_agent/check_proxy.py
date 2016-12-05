#!/usr/bin/env python
# coding:utf8

'''

function : check proxy
author   : Zhangze
date     : 2016-12-04

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
f = open("proxy2.txt")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("^")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    # print proxy_temp
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        print "Ok"
        # break
    except Exception,e:
        # print proxy
        print e
        continue