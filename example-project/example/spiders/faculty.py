# -*- coding: utf-8 -*-                                                                                                  
import scrapy                                                                                                            
from redis import Redis                                                                                                  
from scrapy_redis.spiders import RedisSpider                                                                             
                                                                                                                         
class FacultySpider(RedisSpider):                                                                                           
    name = 'faculty'                                                                                                        
    allowed_domains = ['www.haodf.com/faculty/DE4r08xQdKSLBGazuH5-zTRBJvHg.htm']                                                                                   
    start_urls = ['http://www.haodf.com/faculty/DE4r08xQdKSLBGazuH5-zTRBJvHg.htm']                                                                                
    redis_key = 'hospitalurl'                                                                                                
                                                                                                                         
    def parse(self, response):                                                                                           
        faculty = response.xpath('//a/@href').extract()                                                                 
        r = Redis(host='34.224.8.126',port=6379,password='ClLBIss1709g',db=0)                                            
        for f in faculty:                                                                                               
            if "http://www.haodf.com/faculty" in f:
                     r.lpush('facultyurl', f)  
