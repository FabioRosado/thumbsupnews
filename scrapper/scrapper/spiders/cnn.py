# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from .helper import is_todays_article

class CNNScrapper(XMLFeedSpider):
    name = "cnn"
    start_urls = [
        'http://rss.cnn.com/rss/edition.rss',
        'http://rss.cnn.com/rss/edition_africa.rss',
        'http://rss.cnn.com/rss/edition_americas.rss',
        'http://rss.cnn.com/rss/edition_asia.rss',
        'http://rss.cnn.com/rss/edition_europe.rss',
        'http://rss.cnn.com/rss/edition_meast.rss',
        'http://rss.cnn.com/rss/money_news_international.rss',
        'http://rss.cnn.com/rss/edition_technology.rss',
        'http://rss.cnn.com/rss/edition_space.rss',
        'http://rss.cnn.com/rss/edition_entertainment.rss',
        'http://rss.cnn.com/rss/edition_travel.rss'
        ]
    itertag = 'item'
    
    def parse_node(self, response, node):
        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get()
            }