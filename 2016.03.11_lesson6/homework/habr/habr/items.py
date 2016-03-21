# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def filter_price(value):
    if value.isdigit():
        return value


class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )


class HabrArticle(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    page = scrapy.Field()
    founded = scrapy.Field()