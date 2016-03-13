from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from tutorial.items import ScrapinghubItem

class ScrapinghubSpider(BaseSpider):
    name = "scrapinghub"
    allowed_domains = ["scrapinghub.org", "blog.scrapinghub.com"]
    start_urls = [
        "https://blog.scrapinghub.com/",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        categories = hxs.select('//html//body//div//div//div//ul//li//ul//li//a')

        items = []
        for category in categories:
            item = ScrapinghubItem()
            item['name'] = category.select('text()').extract()
            item['url'] = category.select('@href').extract()

            # print(item['url'][0])
            # print(item['url'][0])
            if "category" in item['url'][0]:
                print(item['url'][0])
                yield Request(url=item['url'][0], callback=self.parse_category)
                # items.append(item)

            # return items

    def parse_category(self, response):
        hxs = HtmlXPathSelector(response)
        # categories = hxs.select('//html//body//div//div//div//h1')
        print(hxs.select('//html//body//div//div//div//div//ul//li//span//a//text()').extract())