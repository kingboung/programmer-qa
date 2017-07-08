# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.selector import Selector
from ProgrammerQA.items import V2exItem


class V2exSpider(scrapy.Spider):
    name = 'V2EX_spider'

    headers = {
        'cache-control': "no-cache",
        'postman-token': "f25380da-6233-c5d0-8c70-e1e76f30d2a6"
    }


    def __init__(self, search='', *args, **kwargs):
        super(V2exSpider, self).__init__(*args, **kwargs)

        logging.info("The search: %s" % search)

        self.search = search
        key_words = search.split(' ')
        url = 'https://www.google.hk/search?q=' + 'site:v2ex.com/t+' + '+'.join(key_words)
        self.start_urls.append(url)


    def parse(self, response):
        selector = Selector(response)

        urls = selector.xpath('//cite/text()').extract()

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

        item = V2exItem()

        item['search'] = self.search
        item['topic'] = selector.xpath("//h1/text()").extract_first()
        item['question'] = selector.xpath('//*[@class="topic_content"]').xpath('string(.)').extract_first()

        answer_selectors = selector.xpath('//*[@id][@class="cell"]')
        for answer_selector in answer_selectors:
            author = answer_selector.xpath('.//strong/a/text()').extract_first()
            authors.append(author)

            time = answer_selector.xpath('.//*[@class="ago"]/text()').extract_first()
            times.append(time)

            content = answer_selector.xpath('.//*[@class="reply_content"]').xpath('string(.)').extract_first()
            contents.append(content)

        for (author, time, content) in zip(authors, times, contents):
            answer = {}
            answer['author'] = author
            answer['time'] = time
            answer['content'] = content
            answers.append(answer)

        item['answers'] = answers
        yield item
