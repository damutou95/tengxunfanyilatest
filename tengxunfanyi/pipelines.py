# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from tengxunfanyi import settings
class TengxunfanyiPipeline(object):
    def __init__(self):
        host = settings.MONGO_HOST
        port = settings.MONGO_PORT
        dbName = settings.MONGO_DBNAME
        colName = settings.MONGO_COLLECTIONNAME
        client = pymongo.MongoClient(host=host, port=port)
        mgd = client[dbName]
        self.post = mgd[colName]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
