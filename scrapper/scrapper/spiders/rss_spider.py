# -*- coding: utf-8 -*-
import sys
import re
import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapy.loader import ItemLoader

from .helper import is_todays_article, transform_date, remove_html

from classifier import NewsHeadlineClassifier

def get_source(source):
    return re.findall(r'Mail Online|Yahoo News|Techworld|CNET News', ', '.join(source))[0]

def get_categories(category):
    if 'Mail Online' in category:
        return category.split(' | ')[0]
    
    if 'CNET News' in category or 'Techworld' in category:
        return 'Tech'
    
    if 'Yahoo News' in category:
        return category.split(' - ')[1]
    

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
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):
        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip()
            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": remove_html(node.xpath('description/text()').get()),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": get_categories(node.xpath('//channel/title/text()').get()),
                "source": get_source(node.xpath('//channel/title/text()').getall()),
                "sentiment": self.classifier.classify(title)
            }

