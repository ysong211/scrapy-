# -*- coding: utf-8 -*-
import os
import urllib

import scrapy
from urllib.parse import urlencode
# from jd.text import l
from jd.items import JdItem
from copy import deepcopy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import pdb
import time

class Jd1Spider(scrapy.Spider):

    def __init__(self):
        # self.browser = webdriver.Chrome()
        super(Jd1Spider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)


    name = 'jdgoods'
    allowed_domains = ['jd.com']
    # start_urls = ['https:jd.com/']
    l = ['手机','电脑']
    start_urls = []

    for keyword in l:
        for page in range(1,2):
            data = {
                'keyword': keyword,
                'enc': 'utf-8',
                'page': page,
                's': (page - 1) * 30,
            }
            # 转换格式
            querise = urlencode(data)
            next_page_url = 'https://search.jd.com/Search?' + querise
            start_urls.append(next_page_url)


    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print("spider closed")
        # import pdb
        # pdb.set_trace()
        self.browser.quit()

    #商品列表页
    def parse(self, response):
        # driver = webdriver.Chrome()
        #
        # driver.get(response.url)
        # driver.implicitly_wait(30)
        # driver.refresh()
        # driver.implicitly_wait(30)
        #
        # js = "window.scrollTo(300,1000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,2000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,3000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,4000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,5000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,6000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # js = "window.scrollTo(200,7000);"
        # driver.execute_script(js)
        # time.sleep(1)
        #
        # driver.close()
        #


        # print(response.body)
        goods = response.css('.gl-item')
        for good in goods:
            item = JdItem()
            # 商品链接
            good_url = good.css('.p-name a::attr(href)').extract_first()
            if good_url is not None:
                good_url = "https:" + good_url
            # 商品信息
            name = good.css('.p-name em::text').extract()
            name = str(name).replace(',', '')

            # 价格
            price = good.css('.p-price i::text').extract_first()
            # 店名
            shop = good.css('.p-shop a::text').extract_first()

            # 获取评价数量
            a = good.css('.p-commit  strong a::text').extract_first()
            b = good.css('.p-commit strong::text').extract_first()
            a = str(a)
            b = str(b)
            commit = a + b

            # 获取是否有二手出售
            used = good.css('.p-commit .spu-link::text').extract_first()
            if used == None:
                used = "二手无售"

            # 获取是否自营
            zy = good.css('.p-icons i::text').extract_first()

            # 图片链接
            img_url = good.css('.p-img a img::attr(src)').extract_first()
            if img_url is not None:
                img_url = "https:" + img_url

            item['name'] = name
            item['price'] = price
            item['shop'] = shop
            item['good_url'] = good_url
            item['commit'] = commit
            item['used'] = used
            item['zy'] = zy
            item['img_url'] = img_url



            yield scrapy.Request(
                url=item['good_url'],
                callback=self.good_temp,
                meta = {'item':deepcopy(item)},
                dont_filter=True,
            )



    # 商品详情页
    def good_temp(self,response):
        time.sleep(1)
        # print(response.body)
        item = response.meta['item']
        item['title'] = response.css('.parameter2 li::text').extract()
        item['shop_url'] = "https:" + response.css('.name a::attr(href)').extract_first()


        yield scrapy.Request(
            url= item['shop_url'],
            callback=self.shop_temp,
            meta = {'item':deepcopy(item)},
            dont_filter=True,
        )

    #商家详情页
    def shop_temp(self,response):
        item = response.meta['item']
        yield item







