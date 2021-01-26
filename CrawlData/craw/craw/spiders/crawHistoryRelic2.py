import scrapy
from craw.items import CrawItem

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
import os
import time

# run in sematic_web/CrawlData/craw

crawHistory2 = "crawHistory2"
historyUrl = "https://dulichvinhphuc.gov.vn/lich-su-van-hoa/cac-di-tich-lich-su-van-hoa.html"
endPage = 10

class historySpider2(scrapy.Spider):
 name = crawHistory2
#  start_urls = [historyUrl]
 def start_requests(self):
  for page in range(1,endPage):
   yield self.make_requests_from_url(historyUrl+'?start=%s' %page)
 def parse(self, response):
  historyUrl = response.xpath('//*[@itemprop="blogPost"]/a/@href').extract()
  print("length"+str(len(historyUrl)))
  storeLink = []
  f = open('link/link.txt','a')
  f.truncate()
  for link in historyUrl:
   print("link:" + 'https://dulichvinhphuc.gov.vn'+link)
   f.write((link.strip()+'\n'))
   storeLink.append(link)
  f.close()
  for link in storeLink:
   yield scrapy.Request('https://dulichvinhphuc.gov.vn'+link, callback=self.saveFile)
 def saveFile(self, response):
  name = response.xpath('//*[@itemprop="name"]/a/text()').extract()
  title = response.xpath('string(//*[@class="articleBody"]/text())').extract()
  name = ''.join(name).strip()
  nameFile = name + '.txt'
  logging.debug("saveFile"+nameFile)
  title = (''.join(title).strip().replace('\n','') + '\n').encode('utf-8')
  content = ''
  contentXpathArrays = response.xpath('//*[@itemprop="articleBody"]//text()').extract()
  for p in contentXpathArrays:
   content = content + ''.join(p)
  content = content.strip().encode('utf-8')
  f = open('historyRelic2/'+nameFile,'wb')
  f.write(content)
  f.close()