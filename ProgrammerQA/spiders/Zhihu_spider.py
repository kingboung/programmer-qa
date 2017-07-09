# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.selector import Selector
from ProgrammerQA.items import ZhihuItem


class ZhihuSpider(scrapy.Spider):
    name = "Zhihu_spider"

    def __init__(self, search='', *args, **kwargs):
        super(ZhihuSpider, self).__init__(*args, **kwargs)

        logging.info("The search: %s" % search)

        self.search = search
        key_words = search.split(' ')
        url = "https://www.zhihu.com/search?type=content&q=" + '+'.join(key_words)
        self.start_urls.append(url)

    def parse(self, response):
        selector = Selector(response).xpath('//div[@class="title"]')

        urls = [ url for url in selector.xpath('./a/@href').extract() if '/question' in url][:5]
        for url in urls:
            url = "https://www.zhihu.com" + url
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        selector = Selector(response)

        authors = []
        times = []
        contents = []
        answers = []

        item = ZhihuItem()

        item['search'] = self.search
        item['topic'] = selector.xpath('//div/h1').xpath('string(.)').extract_first()
        item['question'] = selector.xpath('//div[@class = "QuestionHeader-detail"]').xpath('string(.)').extract_first()

        answer_selectors = selector.xpath('//div[@class="List-item"]/div[@name]')
        for answer_selector in answer_selectors:
            author = answer_selector.xpath('.//*[@itemprop="name"]/@content').extract_first()
            authors.append(author)

            time = answer_selector.xpath('.//div[@class="ContentItem-time"]').xpath('string(.)').extract_first()
            times.append(time)

            content = answer_selector.xpath('.//*[@class="RichText CopyrightRichText-richText"]').xpath('string(.)').extract_first()
            contents.append(content)

        for (author, time, content) in zip(authors, times, contents):
            answer = {}
            answer['author'] = author
            answer['time'] = time
            answer['content'] = content
            answers.append(answer)

        item['answers'] = answers
        yield item
