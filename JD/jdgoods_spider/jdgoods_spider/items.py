# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 要爬取的内容
class JdgoodsSpiderItem(scrapy.Item):

#商品列表
    # 商品信息
    name = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 商铺名称
    shop = scrapy.Field()
    # 商品链接
    good_url = scrapy.Field()
    # 商家链接
    shop_url = scrapy.Field()
    # 商品评价数量
    commit = scrapy.Field()
    #是否有二手
    used = scrapy.Field()
    #是否自营
    goods_icons = scrapy.Field()
    #图片链接
    img_url = scrapy.Field()


#店铺信息
    # 商铺ID
    shop_id = scrapy.Field()
    # 商铺APPID
    # 商品评价评分
    # 服务态度评分
    # 物流速度评分
    # 店铺介绍
    # 开店时间
    # 粉丝数
    # URL
    # HTML代码



#商品详情

    # 产品参数
    # 产品名称
    title = scrapy.Field()
    # /品牌/
    # 产地/
    # 系列/
    # 颜色等商品详情中的根据不同产品设置的参数
    # 、以及文字图片介绍)、
    # (有无)库存、html代码

