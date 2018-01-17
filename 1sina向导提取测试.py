#!usr/bin/python/
# -*-conding:utf-8-*-
import urllib
import urllib.request
import lxml
import lxml.etree

url = "http://news.sina.com.cn/guide/"
data = urllib.request.urlopen(url).read().decode("utf-8")
mytree = lxml.etree.HTML(data)

# 提取大类
biglist = []  # [(titile,url)]
parenturls = mytree.xpath("//h3[@class=\"tit02\"]")
for parenturl in parenturls:
	# print(parenturl.xpath("./a/text()"))
	# print(parenturl.xpath("./a/@href"))
	# print(parenturl.xpath("./span/text()"))
	if len(parenturl.xpath("./span/text()")) == 0 and parenturl.xpath("./a/text()") == 0:
		pass
	elif len(parenturl.xpath("./span/text()")) != 0 or parenturl.xpath("./a/text()") != 0:
		if len(parenturl.xpath("./span/text()")) == 0:
			if len(parenturl.xpath("./a/text()")) == 0:
				pass
			else:
				biglist.append((parenturl.xpath("./a/text()"), parenturl.xpath("./a/@href")))
		else:
			biglist.append((parenturl.xpath("./span/text()"), ""))

for line in biglist:
	print(line)
