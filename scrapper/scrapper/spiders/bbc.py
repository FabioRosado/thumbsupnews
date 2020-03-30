# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from .helper import is_todays_article

class BBCScrapper(XMLFeedSpider):
    name = 'bbc'
    start_urls = ['http://feeds.bbci.co.uk/news/world/rss.xml']
    itertag = 'item'

    def parse_node(self, response, node):
        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get()
            }
