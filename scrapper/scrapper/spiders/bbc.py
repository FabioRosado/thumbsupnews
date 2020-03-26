# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

class BBCScrapper(XMLFeedSpider):
    name = 'bbc'
    start_urls = ['http://feeds.bbci.co.uk/news/world/rss.xml']
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        
        item = {}
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['description'] = node.xpath('description/text()').get()
        
        return item