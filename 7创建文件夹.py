import urllib
import urllib.request
import lxml
import lxml.etree
import os

url = "http://news.sina.com.cn/guide/"
data = urllib.request.urlopen(url).read().decode("utf-8")
mytree = lxml.etree.HTML(data)
parenturls = mytree.xpath("//div[@class=\"clearfix\"]")
rootpath = r"F:\千峰-\day29(scrapy)\SinaChina\data"
for parenturl in parenturls:
	# 遍历所有的大类
	bigdir = ""
	if len(parenturl.xpath("./h3/a/text()")) == 0:
		if len(parenturl.xpath("./h3/span/text()")) == 0:
			print(parenturl.xpath("./h3/text()"))
			bigdir = parenturl.xpath("./h3/text()")[0]
		else:
			print(parenturl.xpath("./h3/span/text()"))
			bigdir = parenturl.xpath("./h3/span/text()")[0]
	else:
		print(parenturl.xpath("./h3/a/text()"))
		bigdir = parenturl.xpath("./h3/a/text()")[0]
	bigpath = rootpath + "//" + bigdir  # 创建大类文件夹
	if not os.path.exists(bigpath):
		os.mkdir(bigpath)

	# 遍历所有的小类
	lines = parenturl.xpath("./ul//li")
	for line in lines:
		print("----", line.xpath("./a/text()"))
		smallpath = bigpath + "//" + line.xpath("./a/text()")[0]  # 创建大类文件夹
		if not os.path.exists(smallpath):
			os.mkdir(smallpath)

		url = line.xpath("./a/@href")[0]
		data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
		mytree = lxml.etree.HTML(data)
		links = mytree.xpath("//div[@class=\"second-nav\"]/div/div//a")
		for line in links:
			print("--------", line.xpath("./text()"))
			basepath = smallpath + "//" + line.xpath("./text()")[0]  # 创建大类文件夹
			if not os.path.exists(basepath):
				os.mkdir(basepath)

	print("")
