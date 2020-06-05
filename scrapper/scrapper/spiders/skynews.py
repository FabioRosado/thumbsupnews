# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier, CategoryClassifier

from .helper import is_todays_article, transform_date, remove_html

class SkyNewsScrapper(XMLFeedSpider):
    name = 'skynews'
    start_urls = [
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
        self.sentiment_classifier = NewsHeadlineClassifier()
        self.category_classifier = CategoryClassifier()
        self.title = ''
    
    def get_category(self, node, classifier):
        category = node.xpath('//channel/title/text()').get().split(" News")[0]
        
        if category.lower() in ['uk', 'world', 'us']:
           return classifier.classify(self.title) 

        return category

    def parse_node(self, response, node):
        self.title = node.xpath('title/text()').get().strip()
        description = remove_html(node.xpath('description/text()').get())

        if is_todays_article(node):
            yield {
                "title": self.title,
                "link": node.xpath('link/text()').get().strip(),
                "description": description,
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": self.get_category(node, self.category_classifier),
                "source": "Sky News",
                "sentiment": self.sentiment_classifier.classify("{} {}".format(self.title, description))
            }
 