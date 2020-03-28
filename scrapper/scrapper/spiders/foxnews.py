# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

class BBCScrapper(XMLFeedSpider):
    name = 'foxnews'
    start_urls = [
        'http://feeds.foxnews.com/foxnews/latest',
        'http://feeds.foxnews.com/foxnews/entertainment',
        'http://feeds.foxnews.com/foxnews/health',
        'http://feeds.foxnews.com/foxnews/section/lifestyle',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.foxnews.com/foxnews/science',
        'http://feeds.foxnews.com/foxnews/tech',
        'http://feeds.foxnews.com/foxnews/internal/travel/mixed',
    ]
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        
        yield {
            "title": node.xpath('title/text()').get(),
            "link": node.xpath('link/text()').get(),
            "description": node.xpath('description/text()').get()
        }
