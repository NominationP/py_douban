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

import json
from bs4 import BeautifulSoup

import time


ss = "https://book.douban.com/subject/1254588/"

print ss.split("/")[4]







