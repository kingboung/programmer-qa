# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.selector import Selector
from ProgrammerQA.items import StackoverflowItem


class StackoverflowSpider(scrapy.Spider):
    name = 'Stackoverflow_spider'


    def __init__(self, search='', *args, **kwargs):
        super(StackoverflowSpider, self).__init__(*args, **kwargs)

        logging.info("The search: %s" % search)

        self.search = search
        key_words = search.split(' ')
        url = 'https://stackoverflow.com/search?q=' + '+'.join(key_words)
        self.start_urls.append(url)


    def parse(self, response):
        selector = Selector(response)

        urls = selector.xpath('//*[@class="result-link"]//a/@href').extract()

        # 如果数目超过5条，只取5条
        if len(urls) >= 5:
            urls = urls[:5]

        for url in urls:
            url = 'https://stackoverflow.com' + url
            yield scrapy.Request(url, callback=self.parse_content)


    def parse_content(self, response):
        selector = Selector(response)

        authors = []
        times = []
        contents = []
        answers = []

        item = StackoverflowItem()

        item['search'] = self.search
        item['topic'] = selector.xpath('//*[@class="question-hyperlink"]/text()').extract_first()
        item['question'] = selector.xpath('//*[@class="post-text"]').xpath('string(.)').extract_first()


        answer_selectors = selector.xpath('//*[@data-answerid]')
        for answer_selector in answer_selectors:

            author = answer_selector.xpath('.//*[@class="user-details"]/a/text()').extract()
            authors.append(author)

            time = answer_selector.xpath('.//*[@class="relativetime"]/@title').extract_first()
            times.append(time)

            content = (answer_selector.xpath('.//*[@class="post-text"]')).xpath('string(.)').extract_first()
            contents.append(content)

        for (author, time, content) in zip(authors, times, contents):
            answer = {}
            answer['author'] = author
            answer['time'] = time
            answer['content'] = content
            answers.append(answer)

        item['answers'] = answers
        yield item
