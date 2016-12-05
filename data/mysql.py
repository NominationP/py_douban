#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='localhost', user='root', passwd='#mJl&dcs.6(O', db='douban', port=8080, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

fr =open('douban_movie_clean.txt','r')

# create
# count = 0
# for line in fr:
#     count += 1
#     print count
#     if count == 1:
#         continue

#     line = line.strip().split('^')
#     cursor.execute('insert into movie(title,url,summary,score) value(%s, %s, %s, %s)',[line[1], line[2], line[9], line[4]])

# update
# cursor.execute('update movie set title=%s, score=%s where id=1',['yibo',9.9])

# Read
# cursor.execute('select * from movie')
# movie = cursor.fetchall()
# print len(movie)
# print movie[0]

# Delete
# cursor.execute('delete from movie')

fr.close()

cursor.close()
db.close()