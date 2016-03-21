
import scrapy

from tutorial.items import ScrapinghubItem


class ScrapinghubSpider(scrapy.Spider):
    name = "scrapinghub"
    allowed_domains = ["scrapinghub.org", "blog.scrapinghub.com"]
    start_urls = [
        "https://blog.scrapinghub.com/",
    ]

    def parse(self, response):
        for category in response.xpath("//html//body//div//div//div//ul//li//ul//li//a"):
            item = ScrapinghubItem()
            item['name'] = category.xpath('text()').extract()
            item['url'] = category.xpath('@href').extract()

            # print(item['url'][0])
            # print(item['url'][0])
            if "category" in item['url'][0]:
                print(item['url'][0])
                yield scrapy.Request(url=item['url'][0], callback=self.parse_category)
                # items.append(item)

            # return items

    def parse_category(self, response):
        # hxs = response.xpath(response)
        # categories = hxs.select('//html//body//div//div//div//h1')
        print(response.xpath('//html//body//div//div//div//div//ul//li//span//a//text()').extract())