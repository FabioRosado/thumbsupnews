# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from .helper import is_todays_article

def get_categories_foxnews(categories):
    """Split categories to get only useful stuff."""
    cat_list = list()
    for category in categories[1:]:
        cat_list.extend(re.sub(r'(fox-news/|fnc|article|Fox News)', '', category).split('/'))
    return list(filter(None, cat_list))

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

    def parse_node(self, response, node):
        feed_type = response.url.split('/')[-1].replace('.rss', '')
        
        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": feed_type.replace('_', ' '),
                "source": "CNN"
            }
