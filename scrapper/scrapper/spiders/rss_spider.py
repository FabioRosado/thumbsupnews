# -*- coding: utf-8 -*-
import sys
import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapy.loader import ItemLoader

from .helper import is_todays_article

from classifier import NewsHeadlineClassifier


class RSSScrapper(XMLFeedSpider):
    name = 'rss'
    start_urls = [
        'https://www.yahoo.com/news/rss',
        'https://www.vox.com/rss/index.xml',
        'http://feeds.reuters.com/reuters/TopNews/',
        'https://www.dailymail.co.uk/articles.rss',
        'https://www.techworld.com/rss',
        'https://www.cnet.com/rss/news',
    ]
    itertag = 'item'

    def __init__(self):
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        if is_todays_article(node):
            title = node.xpath('title/text()').get()
            yield {
                "title": title,
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": node.xpath('//channel/title/text()').getall(),
                "source": node.xpath('//channel/title/text()').getall(),
                "sentiment": self.classifier.classify(title)
            }
