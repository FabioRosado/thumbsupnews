# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

class BBCScrapper(XMLFeedSpider):
    name = 'skynews'
    start_urls = [
        'http://feeds.skynews.com/feeds/rss/home.xml',
        'http://feeds.skynews.com/feeds/rss/uk.xml',
        'http://feeds.skynews.com/feeds/rss/world.xml',
        'http://feeds.skynews.com/feeds/rss/us.xml',
        'http://feeds.skynews.com/feeds/rss/business.xml',
        'http://feeds.skynews.com/feeds/rss/politics.xml',
        'http://feeds.skynews.com/feeds/rss/technology.xml',
        'http://feeds.skynews.com/feeds/rss/entertainment.xml',
        'http://feeds.skynews.com/feeds/rss/strange.xml'
    ]
    itertag = 'item'

    def parse_node(self, response, node):        
        yield {
            "title": node.xpath('title/text()').get(),
            "link": node.xpath('link/text()').get(),
            "description": node.xpath('description/text()').get()
        }
