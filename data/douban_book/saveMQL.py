#!/usr/bin/env python
# coding:utf8

'''
    将清洗的数据插入数据库
    author: Zhangze
    email: 605166577@qq.com
    date: 2016/12/03
'''
import MySQLdb
import MySQLdb.cursors

inputFile = 'book.txt'
fr = open(inputFile, 'r')

firstLine = True

db = MySQLdb.connect(host='localhost', user='root', passwd='#mJl&dcs.6(O', db='douban', port=8889, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

count = 0

for line in fr:
    if firstLine:
        firstLine = False
        continue

    line = line.split('^')

    title= line[0]
    author = line[1]
    pub = line[2]
    date = line[3]
    pages = line[4]
    price = line[5]
    binding = line[6]
    ISBN = line[7]
    rate = line[8]
    vote = line[9]


    cursor.execute('insert into book(title,author,pub,date,pages,price,binding,ISBN,rate,vote) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[title,author,pub,date,pages,price,binding,ISBN,rate,vote])

    count = count + 1
    print count, title

fr.close()
db.close()
cursor.close()