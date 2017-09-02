# -*- coding: utf-8 -*-                                                                                                  
import scrapy                                                                                                            
from redis import Redis                                                                                                  
                                                                                                                         
class HaodfSpider(scrapy.Spider):                                                                                        
    name = 'haodf'                                                                                                       
    allowed_domains = ['haodf.com']                                                                                      
    start_urls = ['http://haodf.com/']                                                                                   
                                                                                                                         
    def parse(self, response):                                                                                           
        area = response.xpath('//*[@id="top"]/div[2]/div[2]/dl/dd[1]/div[1]/ul/li[1]/div/ul/li[*]/a/@href').extract()    
        for a in area:                                                                                                   
            r = Redis(host='34.224.8.126',port=6379,password='ClLBIss1709g',db=0)                                        
            r.lpush('areaurl', a)
