#!usr/bin/python/
# -*-conding:utf-8-*-
import urllib
import urllib.request
import lxml
import lxml.etree

url = "http://news.sina.com.cn/guide/"
data = urllib.request.urlopen(url).read().decode("utf-8")
mytree = lxml.etree.HTML(data)

parenturls = mytree.xpath("//div[@class=\"clearfix\"]")
for parenturl in parenturls:
	if len(parenturl.xpath("./h3/a/text()")) == 0:
		if len(parenturl.xpath("./h3/span/text()")) == 0:
			print(parenturl.xpath("./h3/text()"))
		else:
			print(parenturl.xpath("./h3/span/text()"))
	else:
		print(parenturl.xpath("./h3/a/text()"), parenturl.xpath("./h3/a/@href"))

	lines = parenturl.xpath("./ul//li")
	for line in lines:
		print(line.xpath("./a/text()"), line.xpath("./a/@href"), end="  ")
	print("")
