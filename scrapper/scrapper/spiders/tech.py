# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

from .helper import is_todays_article

class TechCrunchScrapper(XMLFeedSpider):
    name = 'tech'
    start_urls = [
        'http://feeds.feedburner.com/TechCrunch/',
        'https://www.pcworld.com/index.rss',
        'https://lifehacker.com/rss',
        'https://www.engadget.com/rss-full.xml',
        'http://feeds.mashable.com/Mashable',
        'https://gizmodo.com/rss',
        'http://feeds.feedburner.com/Makeuseof',
    ]
    itertag = 'item'

    def parse_node(self, response, node):
        print(node.xpath('category/text()').getall(),)
        # if is_todays_article(node):
        #     yield {
        #         "title": node.xpath('title/text()').get(),
        #         "link": node.xpath('link/text()').get(),
        #         "description": node.xpath('description/text()').get(),
        #         "date": node.xpath('pubDate/text()').get(),
        #         "categories": node.xpath('category/text()').getall(),
        #         "source": node.xpath('//channel/title/text()').get()
        #     }
