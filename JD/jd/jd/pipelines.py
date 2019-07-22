


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# 存储MONGODB
class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    # 从settings拿取配置信息,类方法
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    # 启动爬虫启动数据库
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

        # 插入数据之前清空集合的数据
        # self.db['name'].remove({})

    # 保存到数据库
    def process_item(self, item, spider):
        # name = item.__class__.__name__
        # self.db[name].insert(dict(item))

        # 当价格与商品名称同时相同时不插入数据
        self.db['name'].update({"name":item['name'],"price":item['price'] },{"$set":dict(item)},upsert = True,multi=True)
        return item

    # 爬虫结束的时候关闭数据库
    def close_spider(self, spider):
        self.client.close()