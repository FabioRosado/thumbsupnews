# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider

from .helper import is_todays_article

class WallstreetJournalScrapper(XMLFeedSpider):
    name = 'rss'
    start_urls = [
        'https://feeds.a.dj.com/rss/RSSWorldNews.xml',
        'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
        'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
        'https://feeds.a.dj.com/rss/RSSWSJD.xml',
        'https://feeds.a.dj.com/rss/RSSLifestyle.xml',
        'http://feeds.washingtonpost.com/rss/world',
        'http://feeds.washingtonpost.com/rss/business',
        'http://feeds.washingtonpost.com/rss/lifestyle',
        'http://feeds.washingtonpost.com/rss/entertainment',
        'http://feeds.skynews.com/feeds/rss/home.xml',
        'http://feeds.skynews.com/feeds/rss/uk.xml',
        'http://feeds.skynews.com/feeds/rss/world.xml',
        'http://feeds.skynews.com/feeds/rss/us.xml',
        'http://feeds.skynews.com/feeds/rss/business.xml',
        'http://feeds.skynews.com/feeds/rss/politics.xml',
        'http://feeds.skynews.com/feeds/rss/technology.xml',
        'http://feeds.skynews.com/feeds/rss/entertainment.xml',
        'http://feeds.skynews.com/feeds/rss/strange.xml',
        'https://www.yahoo.com/news/rss',
        'http://feeds.foxnews.com/foxnews/latest',
        'http://feeds.foxnews.com/foxnews/entertainment',
        'http://feeds.foxnews.com/foxnews/health',
        'http://feeds.foxnews.com/foxnews/section/lifestyle',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.foxnews.com/foxnews/science',
        'http://feeds.foxnews.com/foxnews/tech',
        'http://rss.cnn.com/rss/edition.rss',
        'http://rss.cnn.com/rss/edition_europe.rss',
        'http://rss.cnn.com/rss/money_news_international.rss',
        'http://rss.cnn.com/rss/edition_technology.rss',
        'http://rss.cnn.com/rss/edition_space.rss',
        'http://rss.cnn.com/rss/edition_entertainment.rss',
        'http://rss.cnn.com/rss/edition_travel.rss',
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'https://www.vox.com/rss/index.xml',
        'http://feeds.reuters.com/reuters/TopNews/',
        'https://www.dailymail.co.uk/articles.rss',
        'http://feeds.feedburner.com/TechCrunch/'
        'https://www.wired.com/feed/rss',
        'https://www.wired.com/feed/category/science/latest/rss',
        'https://www.pcworld.com/index.rss',
        'https://www.techworld.com/rss',
        'https://lifehacker.com/rss',
        'http://www.engadget.com/rss-full.xml',
        'http://feeds.mashable.com/Mashable',
        'https://gizmodo.com/rss',
        'http://feeds.feedburner.com/Makeuseof',
        'http://www.cnet.com/rss/news',
    ]
    itertag = 'item'

    def parse_node(self, response, node):
        # self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        try:
            if is_todays_article(node):
                yield {
                    "title": node.xpath('title/text()').get(),
                    "link": node.xpath('link/text()').get(),
                    "description": node.xpath('description/text()').get()
                }
        except Exception:
            pass
