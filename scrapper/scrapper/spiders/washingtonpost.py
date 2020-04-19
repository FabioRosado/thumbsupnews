# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

from .helper import is_todays_article, transform_date, remove_html

class WashingtonPostScrapper(XMLFeedSpider):
    name = 'washington'
    start_urls = [
        'http://feeds.washingtonpost.com/rss/world',
        'http://feeds.washingtonpost.com/rss/business',
        'http://feeds.washingtonpost.com/rss/lifestyle',
        'http://feeds.washingtonpost.com/rss/entertainment',
    ]
    itertag = 'item'

    def __init__(self):
        self.classifier = NewsHeadlineClassifier()


    def parse_node(self, response, node):

        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip()
            category = node.xpath('//channel/title/text()').getall()[0]

            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": remove_html(node.xpath('description/text()').get()),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": category,
                "source": "The Washington Post",
                "sentiment": self.classifier.classify(title)
            }
