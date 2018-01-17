#!usr/bin/python/
#-*-conding:utf-8-*-

import urllib
import urllib.request
import lxml
import lxml.etree

url = "http://news.sina.com.cn/c/nd/2018-01-13/doc-ifyqqieu6201946.shtml"
data = urllib.request.urlopen(url).read().decode("utf-8")
mytree = lxml.etree.HTML(data)
title = mytree.xpath('//h1[@class="main-title"]/text()')
print(title)

content = mytree.xpath("//div[@class=\"article\"]//p/text()")
print(content)
for line in content:
	print(line)
