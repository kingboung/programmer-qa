from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pymongo
import logging


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'programmerQA'


def get_collection(spider):
    client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = client.get_database(MONGODB_DB)

    if spider == 'CSDN_spider':
        return db.get_collection('csdn')

    elif spider == 'Stackoverflow_spider':
        return db.get_collection('stackoverflow')

    else:
        return None


def run_spider(spider, search):

    collection = get_collection(spider)

    """为避免影响判断，将数据库中相同search的文档删除"""
    if collection == None:
        logging.warn('No spider matched')
        return None

    collection.remove({'search':search})


    process = CrawlerProcess(get_project_settings())

    process.crawl(spider, search=search)
    process.start()  # the script will block here until the crawling is finished

    """数据库中查询到结果马上返回"""
    while True:
        cursor = collection.find({'search':search})

        if len(cursor):
            return cursor
