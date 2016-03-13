from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst


class ScrapinghubItem(Item):
    name = Field()
    url = Field(default=0, output_processor=TakeFirst())