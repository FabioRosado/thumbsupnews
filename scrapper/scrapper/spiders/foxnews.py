# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

from .helper import is_todays_article, transform_date, remove_html

def get_categories_foxnews(categories):
    """Split categories to get only useful stuff."""
    cat_list = list()
    for category in categories[1:]:
        cat_list.extend(re.sub(r'(fox-news/|fnc|article|Fox News)', '', category).split('/'))
    return ', '.join(list(filter(None, cat_list)))

class FoxNewsScrapper(XMLFeedSpider):
    name = 'foxnews'
    start_urls = [
        'http://feeds.foxnews.com/foxnews/latest',
        'http://feeds.foxnews.com/foxnews/entertainment',
        'http://feeds.foxnews.com/foxnews/health',
        'http://feeds.foxnews.com/foxnews/section/lifestyle',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.foxnews.com/foxnews/science',
        'http://feeds.foxnews.com/foxnews/tech',
    ]
    itertag = 'item'

    def __init__(self):
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):

        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip()
            description = remove_html(node.xpath('description/text()').get())
            yield {
                "title": title, 
                "link": node.xpath('link/text()').get().split(),
                "description": description,
                "date": transform_date(node.xpath('pubDate/text()').get().strip()),
                "categories": get_categories_foxnews(node.xpath('category/text()').getall()),
                "source": "Fox News",
                "sentiment": self.classifier.classify("{} {}".format(title, description))
            }
