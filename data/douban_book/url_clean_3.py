#!/usr/bin/env python
# coding:utf8

'''

function : clean duplicate url of each tag
author   : Zhangze
date     : 2016-12-04

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup


fix_add = '/home/git/fullstack-data-engineer/data/douban_book/url'
read_all_file = (   fix_add+'/url_Culture/url_Culture_book.txt',
                    fix_add+'/url_Life/url_Life_book.txt',
                    fix_add+'/url_Literature/url_Literature_book.txt',
                    fix_add+'/url_Management/url_Management_book.txt',
                    fix_add+'/url_Popular/url_Popular_book.txt',
                    fix_add+'/url_Science/url_Science_book.txt')

write_all_file = (  fix_add+'/url_Culture/url_Culture_book_sim.txt',
                    fix_add+'/url_Life/url_Life_book_sim.txt',
                    fix_add+'/url_Literature/url_Literature_book_sim.txt',
                    fix_add+'/url_Management/url_Management_book_sim.txt',
                    fix_add+'/url_Popular/url_Popular_book_sim.txt',
                    fix_add+'/url_Science/url_Science_book_sim.txt')



def clean_url(read_file,write_file,log_file) :

    lines_seen = set() # holds lines already seen
    outfile = open(write_file, "w")
    for line in open(read_file, "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    num_lines = sum(1 for line in open(read_file))
    num_lines_sim = sum(1 for line in open(write_file))
    current_tag =read_file.split("_")[3]

    print current_tag
    fw_log = open(log_file,'aw')
    line_new = '{:>10}  {:>10}  {:>10}'.format(current_tag, str(num_lines), str(num_lines_sim))
    fw_log.write(line_new+"\n")




for x in xrange(0,6):
    clean_url(read_all_file[x],write_all_file[x],'url_clean_log.txt')


