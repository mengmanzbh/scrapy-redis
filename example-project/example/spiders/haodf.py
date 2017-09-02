# -*- coding: utf-8 -*-
import scrapy


class HaodfSpider(scrapy.Spider):
    name = 'haodf'
    allowed_domains = ['haodf.com']
    start_urls = ['http://haodf.com/']

    def parse(self, response):
        pass
