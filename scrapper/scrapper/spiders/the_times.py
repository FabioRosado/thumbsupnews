# -*- coding: utf-8 -*-
import scrapy
import contextlib

class TheTimesScrapper(scrapy.Spider):
    name = 'the-times'
    start_urls = ['https://thetimes.co.uk/']

    def parse(self, response):
            
        for item in response.css("div.Item"):
            with contextlib.suppress(IndexError):
                yield {
                    "title": item.css("h3.Item-headline > a::text").extract()[0],
                    "url": "https://thetimes.co.uk{}".format(item.css("h3.Item-headline > a::attr(href)").extract_first())
                }  
