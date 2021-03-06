# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zxcs8Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    page_url = scrapy.Field()
    cover = scrapy.Field()
    tag = scrapy.Field()
    rating = scrapy.Field()
    descr = scrapy.Field()
    downloadpage_url = scrapy.Field()
    download_node = scrapy.Field()
    download_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # files_rename = scrapy.Field()
    # images_rename = scrapy.Field()
