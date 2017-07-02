# -*- coding: utf-8 -*-

import pymongo
from scrapy.conf import settings
from scrapy import log

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProgrammerQAPipeline(object):
    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        self.db =conn.get_database(settings['MONGODB_DB'])


    def process_item(self, item, spider):
        answer = {}
        if spider.name == 'CSDN_spider':
            collection = self.db.get_collection('csdn')
            for key, value in item.items():
                answer[key] = value
            collection.insert(answer)

        elif spider.name == 'Stackoverflow_spider':
            collection = self.db.get_collection('stackoverflow')
            for key, value in item.items():
                answer[key] = value
            collection.insert(answer)

        else:
            log.msg("No spider matched", level=log.WARNING)

