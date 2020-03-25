# -*- coding: utf-8 -*-
import scrapy

class TheTimesScrapper(scrapy.Spider):
    name = 'the-times'
    # allowed_domains = ['example.com']
    start_urls = ['https://thetimes.co.uk/', 'https://news.sky.com/',  'https://www.bbc.co.uk/']

    def parse(self, response):
            
        for item in response.css("div.Item"):
            yield {
            "title": item.css("h3.Item-headline > a::text").extract()[0],
            "url": "https://thetimes.co.uk{}".format(item.css("h3.Item-headline > a::attr(href)").extract_first())
        }
