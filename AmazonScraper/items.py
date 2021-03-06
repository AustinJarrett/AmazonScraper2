# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WalmartscraperItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()  
    timestamp = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AmazonscraperItem(scrapy.Item):
    asin = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()  
    ranking = scrapy.Field()
    category = scrapy.Field()
    timestamp = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
