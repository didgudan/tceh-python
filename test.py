# -*- coding: utf-8 -*-

# import os
# import json

# with open('items.json') as data_file:
# 	data = json.load(data_file)

# for it in data:
# 	# print(it[u'href'])
# 	print(it)


# s = u'\u0432\u0447\u0435\u0440\u0430 \u0432 21:01'

# news = s.encode('utf-8')
# print(news)


import datetime
from babel.dates import format_date, format_datetime, format_time, parse_date, parse_pattern

# d = date(2015, 4, 1)
# dd = format_date(d, format='long', locale='ru')

# print(dd.encode('unicode_escape'))


# hub_date = "15.03.2016"
# search_date = datetime.strptime(hub_date, "%d.%m.%Y").date()
# formatted_search_date = format_date(search_date, format='long', locale='ru').encode("utf-8")
# print("type of date is %s, and date is %s " % (type(formatted_search_date) ,formatted_search_date))

# separated_search_date = formatted_search_date.split(" ")

# print(" ".join(separated_search_date))

date1 = u"4 января"
date2 = u"31 декабря 2015"

RU_MONTH_VALUES = {
    u'января': 1,
    u'февраля': 2,
    u'марта': 3,
    u'апреля': 4,
    u'мая': 5,
    u'июня': 6,
    u'июля': 7,
    u'августа': 8,
    u'сентября': 9,
    u'октября': 10,
    u'ноября': 10,
    u'декабря': 12,
}


def int_value_from_ru_month(date_str):
    for k, v in RU_MONTH_VALUES.items():
        date_str = date_str.replace(k, str(v))

    return date_str


# date_str = int_value_from_ru_month(date1)
# date_str += " %s" % str(date.today().year)
# print(date_str)

# date1 = datetime.strptime(date_str, "%d %m %Y")
# print(date1)

# yest = datetime.date.today() - datetime.timedelta(1)
# print(yest.strftime("%d %m %Y"))

# date1_list = date_str.split(" ")
# print(date1_list)

# print(datetime.strptime(date_str, "%d %m %Y"))


# d = datetime.strptime(date1.encode("utf-8"), "%d %B %Y")
# print(d)

# date1_formatted = datetime.strptime(hub_date, "%d.%m.%Y").date()

num = 10
print("page%i"%num)