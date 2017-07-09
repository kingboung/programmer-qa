# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    search = scrapy.Field()
    topic = scrapy.Field()
    answer = scrapy.Field()


class StackoverflowItem(scrapy.Item):
    search = scrapy.Field()
    topic = scrapy.Field()
    question = scrapy.Field()
    answers = scrapy.Field()  # include author, time and content


class V2exItem(scrapy.Item):
    search = scrapy.Field()
    topic = scrapy.Field()
    question = scrapy.Field()
    answers = scrapy.Field()


class OschinaItem(scrapy.Item):
    search = scrapy.Field()
    topic = scrapy.Field()
    question = scrapy.Field()
    answers = scrapy.Field()


class ZhihuItem(scrapy.Item):
    search = scrapy.Field()
    topic = scrapy.Field()
    question = scrapy.Field()
    answers = scrapy.Field()