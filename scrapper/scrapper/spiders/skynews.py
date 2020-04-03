# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

from .helper import is_todays_article

class SkyNewsScrapper(XMLFeedSpider):
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
        'http://feeds.skynews.com/feeds/rss/strange.xml',
    ]
    itertag = 'item'
    
    def __init__(self):
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):
        title = node.xpath('//channel/title/text()').get()
        if is_todays_article(node):
            yield {
                "title": title,
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": title.split(' | ')[0],
                "source": "Sky News",
                "sentiment": self.classifier.classify(title)
            }
 