# -*- coding: utf-8 -*-
import pdb
import urllib
from copy import deepcopy
# import text
import scrapy
from urllib.parse import urlencode
import os
from jdgoods_spider.items import JdgoodsSpiderItem
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import time
from selenium.webdriver.chrome.options import Options

# 解析的方法
class JdgoodsSpider(scrapy.Spider):

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super(JdgoodsSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)


    name = 'jdgoods'
    allowed_domains = ['search.jd.com']
    start_urls = []
    # for keyword in text.l:
    for keyword in ['手机','电脑']:
        for page in range(1, 201):
            data = {
                'keyword': keyword,
                'enc': 'utf-8',
                'page': page,
                's': (page - 1) * 30
            }

            # 转换格式
            querise = urlencode(data)
            next_page_url = 'https://search.jd.com/Search?' + querise
            start_urls.append(next_page_url)


    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()


    # 爬取请求解析
    def parse(self,response):
        goods = response.css('.gl-item')
        for good in goods:
            item = JdgoodsSpiderItem()
            # 商品链接
            good_url = good.css('.p-name a::attr(href)').extract_first()
            if good_url[0:5] != 'https':
                good_url = "https:" + good_url
            # 商品名称
            name = good.css('.p-name em::text').extract()
            name = str(name)
            name = name.replace(',', '')
            # 价格
            price = good.css('.p-price i::text').extract_first()
            # 店名
            shop = good.css('.p-shop a::text').extract_first()
            # 商家链接
            shop_url = good.css('.J_im_icon a::attr(href)').extract_first()
            if shop_url is not None:
                shop_url = "https:" + shop_url
            # 获取评价数量
            a = good.css('.p-commit  strong a::text').extract_first()
            b  = good.css('.p-commit strong::text').extract_first()
            commit = a + b

            # 获取是否有二手出售
            used = good.css('.p-commit .spu-link::text').extract_first()
            if used == None:
                used = "二手无售"

            #获取是否自营
            goods_icons = good.css('.p-icons i::text').extract_first()

            # 图片链接
            img_url = good.css('.p-img a img::attr(src)').extract_first()
            if img_url is not None:
                img_url = "https:" + img_url

            item['name'] = name
            item['price'] = price
            item['shop'] = shop
            item['good_url'] = good_url
            item['shop_url'] = shop_url
            item['commit'] = commit
            item['used'] = used
            item['goods_icons'] = goods_icons
            item['img_url'] = img_url

            yield item





