# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

from .helper import is_todays_article

class FoxNewsScrapper(XMLFeedSpider):
    name = 'foxnews'
    start_urls = [
        'http://feeds.foxnews.com/foxnews/latest',
        'http://feeds.foxnews.com/foxnews/entertainment',
        'http://feeds.foxnews.com/foxnews/health',
        'http://feeds.foxnews.com/foxnews/section/lifestyle',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.foxnews.com/foxnews/science',
        'http://feeds.foxnews.com/foxnews/tech',
    ]
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get()
            }
