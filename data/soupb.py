#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from bs4 import BeautifulSoup

# html = """
# <html>
# <head>
# <title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# soup = BeautifulSoup(html)

# print soup.select('a[class="sister"]')[2].get_text()


css_soup = BeautifulSoup('<p class="body strikeout">dddd</p>')
# print css_soup.select('p[class="body strikeout"]')
print css_soup.select("p.strikeout")
# ["body", "strikeout"]