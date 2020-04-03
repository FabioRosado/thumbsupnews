# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from .spiders.helper import sentiment_serializer


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsHeadline(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    # TODO: Create serializer for date - get only date no hours
    date = scrapy.Field()
    categories = scrapy.Field()
    source = scrapy.Field()
    sentiment = scrapy.Field(serializer=sentiment_serializer)