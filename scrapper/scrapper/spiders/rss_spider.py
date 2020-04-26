# -*- coding: utf-8 -*-
import sys
import re
import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapy.loader import ItemLoader

from .helper import is_todays_article, transform_date, remove_html

from classifier import NewsHeadlineClassifier, CategoryClassifier


class RSSScrapper(XMLFeedSpider):
    name = 'rss'
    start_urls = [
        'https://www.yahoo.com/news/rss',
        'https://www.dailymail.co.uk/articles.rss',
        'https://www.techworld.com/rss',
        'https://www.cnet.com/rss/news',
    ]
    itertag = 'item'

    def __init__(self):
        self.sentiment_classifier = NewsHeadlineClassifier()
        self.category_classifier = CategoryClassifier()
    
    def get_source(self, source):
        return re.findall(r'Mail Online|Yahoo News|Techworld|CNET News', ', '.join(source))[0]

    def parse_node(self, response, node):
        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip().replace('- CNET', '')
            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": remove_html(node.xpath('description/text()').get()),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": self.category_classifier.classify(title),
                "source": self.get_source(node.xpath('//channel/title/text()').getall()),
                "sentiment": self.sentiment_classifier.classify(title)
            }
