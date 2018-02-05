# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    商品名称=scrapy.Field()
    商品价格=scrapy.Field()
    商品链接=scrapy.Field()
    店铺链接=scrapy.Field()
    商品评论数=scrapy.Field()
