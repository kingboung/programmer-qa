# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.selector import Selector
from ProgrammerQA.items import CsdnItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class CsdnSpider(scrapy.Spider):
    name = 'CSDN_spider'
    url_selected = []
    page = 1

    headers = {
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        'cache-control': "no-cache",
        'postman-token': "4bb8f7c1-b202-0331-1c5f-b56b458adee3"
    }

    def __init__(self, search='', *args, **kwargs):
        super(CsdnSpider, self).__init__(*args, **kwargs)

        logging.info("The search: %s" % search)

        self.search = search
        key_words = search.split(' ')
        self.initial_url = 'http://so.csdn.net/so/search/s.do?q=' + '+'.join(key_words)
        self.start_urls.append(self.initial_url)

    #  从搜索页爬取出标题
    def clean_topics_from_blogs(self, blogs):
        topics = []
        for blog in blogs:
            topic = ''.join(re.findall(r'(?<= \t).*(?=\r)', blog))
            topics.append(topic)
        return topics


    def parse(self, response):
        selector = Selector(response).xpath('//dt')

        # 只选取五条的结果
        blogs = selector.xpath('string(.)').extract()

        topics = self.clean_topics_from_blogs(blogs)
        urls = selector.xpath('./a[1]/@href').extract()

        # CSDN博客才符合解析要求(CSDN下载，CSDN极客头条这些不满足解析格式)
        for (topic, url) in zip(topics, urls):
            if 'CSDN博客' in topic:
                self.url_selected.append(url)

        if len(self.url_selected) >= 5:
            for url in self.url_selected[:5]:
                yield scrapy.Request(url, callback=self.parse_content)

        else:
            # 本页没有下一页
            if selector.xpath('//*[@class="btn btn-xs btn-default btn-next"]') == 0:
                for url in self.url_selected:
                    yield scrapy.Request(url, callback=self.parse_content)
            # 本页有下一页
            else:
                self.page += 1
                url = self.initial_url + '&p=%d' % self.page
                yield scrapy.Request(url, callback=self.parse)


    def parse_content(self, response):
        selector = Selector(response)

        answer = {}

        item = CsdnItem()

        item['search'] = self.search
        item['topic'] = (selector.xpath('//*[@id="article_details"]//a')).xpath('string(.)').extract()[0].encode('utf-8')
        answer['author'] = selector.xpath('//*[@class="user_name"]/text()').extract_first()
        answer['time'] = selector.xpath('//*[@class="link_postdate"]/text()').extract_first()
        answer['content'] = (selector.xpath('//*[@id="article_content"]')).xpath('string(.)').extract_first().encode('utf-8')

        item['answer'] = answer

        return item
