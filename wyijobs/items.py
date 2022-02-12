# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WyijobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    department = scrapy.Field()
    type = scrapy.Field()
    city = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()
    describe = scrapy.Field()
    require = scrapy.Field()

