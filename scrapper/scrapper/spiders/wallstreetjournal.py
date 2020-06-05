# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.spiders import XMLFeedSpider
from classifier import NewsHeadlineClassifier, CategoryClassifier

from .helper import is_todays_article, transform_date, remove_html


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
        self.sentiment_classifier = NewsHeadlineClassifier()
        self.category_classifier = CategoryClassifier()
    
    def get_categories(self, categories, title, classifier):
        category = list(set(categories))[0]

        if category == 'Future of Everything':
            return 'Tech'

        if 'Nguyen' in category:
            return "Personal Technology"

        if category == 'Half Full':
            return "Entertainment"
        return classifier.classify(title)

    def parse_node(self, response, node):
        sel = Selector(response)
        sel.register_namespace("wsj", "http://dowjones.net/rss/")

        if is_todays_article(node):
            title = node.xpath('title/text()').get().strip()
            description = remove_html(node.xpath('description/text()').get())
            yield {
                "title": title,
                "link": node.xpath('link/text()').get().strip(),
                "description": description,
                "date": transform_date(node.xpath('pubDate/text()').get()),
                "categories": self.get_categories(sel.xpath('//wsj:articletype/text()').getall(), title, self.category_classifier),
                "source": "Wallstreet Journal",
                "sentiment": self.sentiment_classifier.classify("{} {}".format(title, description))
            }
