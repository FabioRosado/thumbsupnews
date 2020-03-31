# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

from .helper import is_todays_article

class WashingtonPostScrapper(XMLFeedSpider):
    name = 'washington'
    start_urls = [
        'http://feeds.washingtonpost.com/rss/world',
        'http://feeds.washingtonpost.com/rss/business',
        'http://feeds.washingtonpost.com/rss/lifestyle',
        'http://feeds.washingtonpost.com/rss/entertainment',
    ]
    itertag = 'item'

    def parse_node(self, response, node):

        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": node.xpath('//channel/title/text()').getall(),
                "source": "The Washington Post"
            }
