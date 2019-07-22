# -*- coding: utf-8 -*-
import scrapy
import pymongo
import scrapy
from pymongo import MongoClient
import scrapy
from urllib.parse import urlencode
from jdgoods_spider.items import JdgoodsSpiderItem
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


#创建数据库连接
conn = MongoClient("localhost",27017)
#创建数据库对象
db = conn.jdgoods
#获取集合对象
myset = db.name



class JdshopSpider(scrapy.Spider):
    def __init__(self):
        self.browser = webdriver.Chrome()
        super(JdshopSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    name = 'jdshop'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    # 创建数据库连接
    client = MongoClient("localhost", 27017)
    # 创建数据库对象
    db = client.jdgoods
    # 获取集合对象
    collection = db['name']
    cursor = collection.find({},{'shop_url': 1, '_id': 0})
    for i in cursor:
        start_urls.append(i['shop_url'])
        print(start_urls)


    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def parse(self, response):
        item = JdgoodsSpiderItem()
