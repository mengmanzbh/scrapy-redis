# -*- coding: utf-8 -*-                                                                                                  
import scrapy                                                                                                            
from redis import Redis                                                                                                  
from scrapy_redis.spiders import RedisSpider                                                                             
                                                                                                                         
class AreaSpider(RedisSpider):                                                                                           
    name = 'area'                                                                                                        
    allowed_domains = ['sh.haodf.com']                                                                                   
    start_urls = ['http://sh.haodf.com/']                                                                                
    redis_key = 'areaurl'                                                                                                
                                                                                                                         
    def parse(self, response):                                                                                           
        hospital = response.xpath('//a/@href').extract()                                                                 
        r = Redis(host='34.224.8.126',port=6379,password='ClLBIss1709g',db=0)                                            
        for h in hospital:                                                                                               
            if "http://www.haodf.com/hospital" in h:                                                                     
                     r.lpush('hospitalurl', h)
