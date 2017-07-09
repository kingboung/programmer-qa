# -*- coding: utf-8 -*-

import pymongo
import logging
from scrapy.utils.project import get_project_settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProgrammerQAPipeline(object):
    def __init__(self):
        settings = get_project_settings()
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

        elif spider.name == 'V2EX_spider':
            collection = self.db.get_collection('v2ex')
            for key, value in item.items():
                answer[key] = value
            collection.insert(answer)

        elif spider.name == 'Oschina_spider':
            collection = self.db.get_collection('oschina')
            for key, value in item.items():
                answer[key] = value
            collection.insert(answer)

        elif spider.name == 'Zhihu_spider':
            collection = self.db.get_collection('zhihu')
            for key, value in item.items():
                answer[key] = value
            collection.insert(answer)

        else:
            logging.warning("No spider matched")

