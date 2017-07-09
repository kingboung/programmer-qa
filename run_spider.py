# -*- coding:utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

import pymongo
import sys

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'programmerQA'
SPIDERS = ['CSDN_spider', 'Stackoverflow_spider', 'V2EX_spider', 'Oschina_spider']


"""为避免影响判断，将数据库中相同search的文档删除"""
def remove_duplicate(search):
    client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = client.get_database(MONGODB_DB)

    for spider in SPIDERS:
        if spider == 'CSDN_spider':
            collection = db.get_collection('csdn')
            collection.remove({'search': search})

        if spider == 'Stackoverflow_spider':
            collection = db.get_collection('stackoverflow')
            collection.remove({'search': search})

        if spider == 'V2EX_spider':
            collection = db.get_collection('v2ex')
            collection.remove({'search': search})

        if spider == 'Oschina_spider':
            collection = db.get_collection('oschina')
            collection.remove({'search': search})


def get_cursors(search):
    client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = client.get_database(MONGODB_DB)

    cursors = {}

    cursors['csdn'] = db.get_collection('csdn').find({'search': search})
    cursors['stackoverflow'] = db.get_collection('stackoverflow').find({'search': search})
    cursors['v2ex'] = db.get_collection('v2ex').find({'search': search})
    cursors['oschina'] = db.get_collection('oschina').find({'search': search})

    return cursors


def run_spider(search):

    settings = get_project_settings()

    configure_logging()
    process = CrawlerProcess(settings=settings)

    for spider in SPIDERS:
        process.crawl(spider, search=search)

    process.start()


if __name__ == '__main__':
    args = sys.argv
    # 获取爬取问题
    search = args[1]

    run_spider(search)