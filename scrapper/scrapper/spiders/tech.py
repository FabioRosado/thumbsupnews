# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

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

    def __init__(self):
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):

        if is_todays_article(node):
            title = node.xpath('title/text()').get()

            yield {
                "title": title,
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": node.xpath('category/text()').getall(),
                "source": node.xpath('//channel/title/text()').get(),
                "sentiment": self.classifier.classify(title)
            }
