# -*- coding: utf-8 -*-
import pymongo
import scrapy
from pymongo import MongoClient
import scrapy
from urllib.parse import urlencode
from jdgoods_spider.items import JdgoodsSpiderItem
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class JdgoodsTempSpider(scrapy.Spider):
    def __init__(self):
        self.browser = webdriver.Chrome()
        super(JdgoodsTempSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    name = 'jdgoods_temp'
    allowed_domains = ['jd.com']
    start_urls = []
    # 创建数据库连接
    client = MongoClient("localhost", 27017)
    # 创建数据库对象
    db = client.jdgoods
    # 获取集合对象
    collection = db['name']
    cursor = collection.find({}, {'good_url': 1, '_id': 0})
    for i in cursor:
        start_urls.append(i['good_url'])
        print(start_urls)


    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()


    # 爬取请求解析
    def parse(self,response):
        item = JdgoodsSpiderItem()

        # 价格
        price = response.css('.price::text').extract_first()
        # 店名
        shop = response.css('.name a::text').extract_first()
        # 商家链接
        shop_url = 'https' + response.css('.name a::attr(href)').extract_first()
        # 获取评价数量
        commit = response.css('.count::text').extract_first()
        # 商品名称
        name = response.css('.parameter2 li::text').extract_first()
        #商品编号
        name_id = response.css('.parameter2 li::text').extract()[1]
        #品牌
        a = response.css('#parameter-brand li::text').extract_first()
        b = response.css('#parameter-brand li a::text').extract_first()
        # brand = a + b
        #参数
        titles = response.css('.parameter2 li::text').extract()
