# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

from .helper import is_todays_article, transform_date, remove_html

class TechCrunchScrapper(XMLFeedSpider):
    name = 'tech'
    start_urls = [
        'http://feeds.feedburner.com/TechCrunch/',
        'https://www.pcworld.com/index.rss',
        'https://lifehacker.com/rss',
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
            
            description = remove_html(node.xpath('description/text()').get())

            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": description.replace('Read more...', ''),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": "Tech",
                "source": node.xpath('//channel/title/text()').get(),
                "sentiment": self.classifier.classify(title)
            }
