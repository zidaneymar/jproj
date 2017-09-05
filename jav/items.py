# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mv_name = scrapy.Field()
    mv_id = scrapy.Field()
    mv_pic = scrapy.Field()
    
