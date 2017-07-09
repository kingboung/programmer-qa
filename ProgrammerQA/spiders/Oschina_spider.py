# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.selector import Selector
from ProgrammerQA.items import OschinaItem


class OschinaSpider(scrapy.Spider):
    name = 'Oschina_spider'
    domain = 'https://www.oschina.net/search'

    def __init__(self, search='', *args, **kwargs):
        super(OschinaSpider, self).__init__(*args, **kwargs)

        logging.info("The search: %s" % search)

        self.search = search
        key_words = search.split(' ')
        url = 'https://www.oschina.net/search?scope=bbs&q=' + '+'.join(key_words)
        self.start_urls.append(url)


    def parse(self, response):
        url = self.domain + str(re.findall(r'(?<=href=").*(?=";)', response.text)[0])

        yield scrapy.Request(url, callback=self.parse_url)


    def parse_url(self, response):
        selector = Selector(response)

        urls = selector.xpath('//*[@class="url"]/text()').extract()

        # 如果数目超过5条，只取5条
        if len(urls) >= 5:
            urls = urls[:5]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_content)


    def parse_content(self, response):
        selector = Selector(response)

        authors = []
        times = []
        contents = []
        answers = []

        item = OschinaItem()

        item['search'] = self.search
        item['topic'] = selector.xpath('//*[@class="question-title-link"]/text()').extract_first()
        item['question'] = selector.xpath('//*[@class="wrap cke_editable cke_editable_themed cke_contents_ltr cke_show_borders"]').xpath('string(.)').extract_first()


        answer_selectors = selector.xpath('//*[@class="box answer "]')
        for answer_selector in answer_selectors:

            author = answer_selector.xpath('.//*[@class="wrap user_name"]/text()').extract_first()
            authors.append(author)

            time = answer_selector.xpath('.//*[@class="reply-time"]/@title').extract_first()
            times.append(time)

            content = answer_selector.xpath('.//*[@class="wrap answer_detail"]').xpath('string(.)').extract_first()
            contents.append(content)

        for (author, time, content) in zip(authors, times, contents):
            answer = {}
            answer['author'] = author
            answer['time'] = time
            answer['content'] = content
            answers.append(answer)

        item['answers'] = answers
        yield item
