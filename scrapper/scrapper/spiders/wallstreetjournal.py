# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier

from .helper import is_todays_article

class WallstreetJournalScrapper(XMLFeedSpider):
    name = 'wallstreet'
    start_urls = [
        'https://feeds.a.dj.com/rss/RSSWorldNews.xml',
        'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
        'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
        'https://feeds.a.dj.com/rss/RSSWSJD.xml',
        'https://feeds.a.dj.com/rss/RSSLifestyle.xml',

    ]
    itertag = 'item'

    def __init__(self):
        self.classifier = NewsHeadlineClassifier()

    def parse_node(self, response, node):
        sel = Selector(response)
        sel.register_namespace("wsj", "http://dowjones.net/rss/")

        if is_todays_article(node):
            title = node.xpath('title/text()').get()    

            yield {
                "title": title,
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": sel.xpath('//wsj:articletype/text()').getall(),
                "source": "Wallstreet Journal",
                "sentiment": self.classifier.classify(title)
            }
