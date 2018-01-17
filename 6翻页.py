#!usr/bin/python/
# -*-conding:utf-8-*-
# !usr/bin/python/
# -*-conding:utf-8-*-

import urllib
import urllib.request
import lxml
import lxml.etree


def getpage(url):
	# print(url)
	# print(url.split("/"))
	data = urllib.request.urlopen(url).read().decode("gbk")
	mytree = lxml.etree.HTML(data)
	urllist = url.split("/")
	nexturl = mytree.xpath("//span[@class=\"pagebox_next\"]/a/@href")[0]
	nexturl = nexturl[2:]
	newurl = ""
	for i in range(len(urllist) - 1):
		newurl += urllist[i]
		newurl += "/"
	newurl += nexturl
	print("newurl==", newurl)

	if len(mytree.xpath("//ul[@class=\"list_009\"]//li")) == 0:  # 没有数据终止递归
		pass
	else:
		getpage(newurl)


getpage("http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml")
