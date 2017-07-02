# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.selector import Selector
from ProgrammerQA.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = 'CSDN_spider'

    headers = {
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        'cache-control': "no-cache",
        'postman-token': "4bb8f7c1-b202-0331-1c5f-b56b458adee3"
    }

    def __init__(self, question='', *args, **kwargs):
        super(CsdnSpider, self).__init__(*args, **kwargs)

        # logging.info("The question is:" + question)
        self.question = question
        key_words = question.split(' ')
        url = 'http://so.csdn.net/so/search/s.do?q=' + '+'.join(key_words)
        self.start_urls.append(url)

    #  从搜索页爬取出标题
    # def clean_topics_from_blogs(self, blogs):
    #     topics = []
    #     for blog in blogs:
    #         topic = ''.join(re.findall(r'(?<= \t).*(?=\r)', blog))
    #         topics.append(topic)
    #     return topics


    def parse(self, response):
        selector = Selector(response).xpath('//dt')

        # 只选取前五条的结果
        # blogs = selector.xpath('string(.)').extract()[:5]
        # topics = self.clean_topics_from_blogs(blogs)
        # for (topic, url) in zip(topics, urls):
        #     yield scrapy.Request(url, callback=self.parse_content)

        urls = selector.xpath('./a[1]/@href').extract()[:5]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        selector = Selector(response)
        item = CsdnItem()
        item['question'] = self.question
        item['topic'] = (selector.xpath('//*[@id="article_details"]//a')).xpath('string(.)').extract()[0].encode(
            'utf-8')
        item['author'] = selector.xpath('//*[@class="user_name"]/text()').extract_first()
        item['time'] = selector.xpath('//*[@class="link_postdate"]/text()').extract_first()
        item['content'] = (selector.xpath('//*[@id="article_content"]')).xpath('string(.)').extract_first().encode(
            'utf-8')
        # logging.info(
        #     'Topic: ' + item['question'] + '\n' +
        #     'Author: ' + item['author'] + '\n' +
        #     'Time: ' + item['time'] + '\n' +
        #     'Content: ' + item['content']
        # )
        return item
