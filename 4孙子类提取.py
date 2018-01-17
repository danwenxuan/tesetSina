# !usr/bin/python/
# -*-conding:utf-8-*-
import urllib
import urllib.request
import lxml
import lxml.etree

url = "http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml"
data = urllib.request.urlopen(url).read().decode("gbk")

mytree = lxml.etree.HTML(data)

links = mytree.xpath("//ul[@class=\"list_009\"]//li")
for line in links:
	print(line.xpath("./a/@href"), line.xpath("./a/text()"), line.xpath("./span/text()"))
