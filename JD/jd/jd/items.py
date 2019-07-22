# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    title = scrapy.Field()
    shop_url = scrapy.Field()
    # 商品列表
    # 商品信息
    name = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 商铺名称
    shop = scrapy.Field()
    # 商品链接
    good_url = scrapy.Field()
    # 商品评价数量
    commit = scrapy.Field()
    # 是否有二手
    used = scrapy.Field()
    # 是否自营
    zy = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()

    # 店铺信息
    # 商铺ID
    shop_id = scrapy.Field()


