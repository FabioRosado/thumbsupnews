# -*- coding: utf-8 -*-
import contextlib
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier, CategoryClassifier

from .helper import is_todays_article, transform_date, remove_html


class CNNScrapper(XMLFeedSpider):
    name = 'cnn'
    start_urls = [
        'http://rss.cnn.com/rss/edition.rss',
        'http://rss.cnn.com/rss/edition_europe.rss',
        'http://rss.cnn.com/rss/money_news_international.rss',
        'http://rss.cnn.com/rss/edition_technology.rss',
        'http://rss.cnn.com/rss/edition_space.rss',
        'http://rss.cnn.com/rss/edition_entertainment.rss',
        'http://rss.cnn.com/rss/edition_travel.rss',
    ]
    itertag = 'item'

    def __init__(self):
        self.sentiment_classifier = NewsHeadlineClassifier()
        self.category_classifier = CategoryClassifier()
        self.title = ''

    def get_category(self, response, title):
        feed_type = response.url.split('/')[-1].replace('.rss', '')
        category = feed_type.replace('edition_', '').title()
        
        if category in ["Edition", "Europe"]:
            return self.category_classifier.classify(title)
        return category

    def parse_node(self, response, node):
        
        if is_todays_article(node):
            self.title = node.xpath('title/text()').get().strip()
            
            
            with contextlib.suppress(TypeError): 
                description = remove_html(node.xpath('description/text()').get())

            yield {
                "title": self.title,
                "link": node.xpath('link/text()').get().strip(),
                "description": description,
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": self.get_category(response, self.title),
                "source": "CNN",
                "sentiment": self.sentiment_classifier.classify("{} {}".format(self.title, description))
            }
