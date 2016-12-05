#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

fr = open('xyj.txt','r')

characers = []
stat = {}

for line in fr:
  line = line.strip()

  if len(line) == 0:
    continue
  line = unicode(line)

  for x in xrange(0, len(line)):
    if line[x] in [' ', '\t', '\n', '，', '。', ',', '.', '-', '：', '、', '“', '！', '”', '？']:
      continue

    if not line[x] in characers:
        characers.append(line[x])

    if not stat.has_key(line[x]):
        stat[line[x]] = 0
    stat[line[x]] += 1


fw = open('result.json', 'w')
fw.write(json.dumps(stat))
fw.close

stat = sorted(stat.iteritems(), key=lambda d:d[1], reverse=True)

fw = open('result.csv', 'w')
for item in stat:
  fw.write(item[0] + ','+str(item[1]) + '\n')
fw.close()

fr.close()
