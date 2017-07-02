# -*- coding: utf-8 -*-

import pymongo
from scrapy.conf import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        db =conn.get_database(settings['MONGODB_DB'])
        self.collection = db.get_collection(settings['MONGODB_COLLECTION'])

    def process_item(self, item, spider):
        article = {}
        for key, value in item.items():
            article[key] = value
        self.collection.insert(article)

