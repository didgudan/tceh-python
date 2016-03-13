import scrapy


class SpiderItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class Spider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = [
        "https://blog.scrapinghub.com/",
    ]

    def parse(self, response):
      for url in response.css('ul li a:attr("href")')