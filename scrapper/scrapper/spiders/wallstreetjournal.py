# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier, CategoryClassifier

from .helper import is_todays_article, transform_date, remove_html


def get_categories(categories):
    category = list(set(categories))[0]

    if category == 'Future of Everything':
        return 'Tech'

    if 'Nguyen' in category:
        return "Personal Technology"

    if category == 'Half Full':
        return "Entertainment"
    return category


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
            title = node.xpath('title/text()').get().strip()

            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": remove_html(node.xpath('description/text()').get()),
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": get_categories(sel.xpath('//wsj:articletype/text()').getall()),
                "source": "Wallstreet Journal",
                "sentiment": self.classifier.classify(title)
            }
