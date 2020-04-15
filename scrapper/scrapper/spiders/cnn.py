# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

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
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):
        feed_type = response.url.split('/')[-1].replace('.rss', '')
        
        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip()

            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": remove_html(node.xpath('description/text()').get()),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": feed_type.replace('_', ' '),
                "source": "CNN",
                "sentiment": self.classifier.classify(title)
            }
