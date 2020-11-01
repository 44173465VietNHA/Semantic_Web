import scrapy
from craw.items import CrawItem

firstCraw = "firstCraw"
firstUrl = "https://www.maxreading.com/sach-hay/danh-lam-thang-canh.html"

class FirstSpider(scrapy.Spider):
 name = firstCraw
 start_urls = [firstUrl]
 def parse(self, response):
  scenicSpots = response.xpath('//*[@id="content"]/div/div[1]/div/table/tbody/tr/td[2]/a/@href').extract()
  for link in scenicSpots:
   yield scrapy.Request(link.replace('..', 'https://www.maxreading.com'), callback=self.saveFile)
 def saveFile(self, response):
  name = response.xpath('//*[@id="content"]/div/div[1]/div/h3/text()').extract()
  content = response.xpath('//*[@id="chapter"]/.//text()').extract()
  strName = ''.join(name)
  nameFile = strName.strip()+'.txt'
  allContent = ''
  for text in content:
   allContent = allContent + ''.join(text).strip()
  allContent = allContent.strip().encode('utf-8')
  f = open('scenicSpots/'+nameFile,'wb')
  f.write(allContent)
  f.close()