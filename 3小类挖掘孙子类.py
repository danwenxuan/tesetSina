
#!usr/bin/python/
#-*-conding:utf-8-*-
import urllib
import urllib.request
import lxml
import lxml.etree

url = "http://mil.news.sina.com.cn/"
data = urllib.request.urlopen(url).read().decode("utf-8")
mytree = lxml.etree.HTML(data)

lines = mytree.xpath("//div[@class=\"second-nav\"]/div/div//a")
for line in lines:
	print(line.xpath("./@href"),line.xpath("./text()"))
