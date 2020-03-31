# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

from .helper import is_todays_article

class RSSScrapper(XMLFeedSpider):
    name = 'rss'
    start_urls = [
        'https://www.yahoo.com/news/rss',
        'https://www.vox.com/rss/index.xml',
        'http://feeds.reuters.com/reuters/TopNews/',
        'https://www.dailymail.co.uk/articles.rss',
        'https://www.techworld.com/rss',
        'https://www.cnet.com/rss/news',
    ]
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        if is_todays_article(node):
            yield {
                "title": node.xpath('title/text()').get(),
                "link": node.xpath('link/text()').get(),
                "description": node.xpath('description/text()').get(),
                "date": node.xpath('pubDate/text()').get(),
                "categories": node.xpath('//channel/title/text()').getall(),
                "source": node.xpath('//channel/title/text()').getall()
            }
