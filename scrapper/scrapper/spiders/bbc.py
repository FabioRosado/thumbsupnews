# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

class BBCScrapper(XMLFeedSpider):
    name = 'bbc'
    start_urls = ['http://feeds.bbci.co.uk/news/world/rss.xml']
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        
        yield {
            "title": node.xpath('title/text()').get(),
            "link": node.xpath('link/text()').get(),
            "description": node.xpath('description/text()').get()
        }
