# -*- coding: utf-8 -*-                                                                                                  
import scrapy                                                                                                            
from redis import Redis                                                                                                  
from scrapy_redis.spiders import RedisSpider                                                                             
                                                                                                                         
class DoctorSpider(RedisSpider):                                                                                           
    name = 'doctor'                                                                                                        
    allowed_domains = ['www.haodf.com/faculty/DE4r08xQdKSLBGazuH5-zTRBJvHg.htm']                                                                                   
    start_urls = ['http://www.haodf.com/faculty/DE4r08xQdKSLBGazuH5-zTRBJvHg.htm']                                                                                
    redis_key = 'facultyurl'                                                                                                
                                                                                                                         
    def parse(self, response):
        table = response.xpath('//*[@id="doc_list_index"]')
        doctor = table.xpath('//a[@class="name"]/@href').extract() 
        r = Redis(host='34.224.8.126',port=6379,password='ClLBIss1709g',db=0)                                            
        for d in doctor:                                                                                               
            if "http://www.haodf.com/doctor" in d:
                     r.lpush('doctorurl', d)                                                                 

