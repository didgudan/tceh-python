# -*- coding: utf-8 -*-

import re
import scrapy
import datetime
import json

from habr.items import HabrArticle
from habr.utils import int_value_from_ru_month, MAX_HABR_PAGE

# Задача: написать веб паука, который бы собирал статьи с habrahabr.ru по заданным разделам за указанную дату.
# Разбить на шаги можно так:
# 1) Программа получает ссылку на пользователя
# 2) Паук находит все хабы, на которые подписан пользователь
# 3) Паук скачивает все статьи из хаба за определенную дату


class HabrSpider(scrapy.Spider):
    name = "habr"
    allowed_domains = ["habrahabr.ru"]

    def __init__(self, filename=None):
        self.start_urls = []
        if not filename:
            print "You must pass to me filename=filename.json file as argument!"
            exit()

        with open(filename) as data_file:
            input_data = json.load(data_file)

        self.start_urls.append(input_data['url'])
        self.search_date = datetime.datetime.strptime(input_data['date'], "%d.%m.%Y").date()
        self.maximum_page_found = False

    def parse(self, response):
        out = response.xpath('//ul[@id="hubs_data_items"]')
        all_user_hubs = re.findall(r'/hub/.*', out.extract_first())

        for raw_hub in all_user_hubs:
            hub_url = re.findall(r'^(/hub/.*)/">.*', raw_hub)[0].encode("utf-8")

            full_http_hubs_path = response.urljoin(hub_url)
            full_http_hubs_path += "/all"
            yield scrapy.Request(url=full_http_hubs_path, callback=self.parse_hub)
        # yield scrapy.Request(url="https://habrahabr.ru/hub/crypto/all/", callback=self.parse_hub)

    def make_articles_from_page(self, response):
        articles = []
        top_element = response.selector.css(".shortcuts_item")
        for elem in top_element:
            post_time = elem.css(".published").extract()

            if len(post_time) == 0:
                continue

            # get from full datetime string with divs just datetime
            just_datetime_string = re.findall(r'<div class="published">(.*)</div>', post_time[0])[0].strip()

            post_time_list = just_datetime_string.split(" ")
            if len(post_time_list) == 3:
                post_date_str = datetime.date.today() - datetime.timedelta(1)
                post_date_str = post_date_str.strftime("%d %m %Y")
            if len(post_time_list) == 4:
                post_date_str = " ".join(post_time_list[0:2])
                post_date_str += " %s" % str(datetime.date.today().year)
            elif len(post_time_list) == 5:
                post_date_str = " ".join(post_time_list[0:3])

            post_date_str = int_value_from_ru_month(post_date_str)
            post_date = datetime.datetime.strptime(post_date_str, "%d %m %Y").date()

            # if search date
            if self.search_date > post_date:
                self.maximum_page_found = True
                return articles

            article = HabrArticle()
            article['title'] = elem.css('.post_title').xpath("text()").extract()
            article['text'] = elem.css('.html_format').xpath("text()").extract()
            article['date'] = post_date
            articles.append(article)

        return articles

    def parse_hub(self, response):
        base_page = response.url

        for num in range(1, MAX_HABR_PAGE+1):
            current_page = "".join([base_page, "page%i" %num])
            if self.maximum_page_found is True:
                break

            yield scrapy.Request(url=current_page, callback=self.make_articles_from_page)
