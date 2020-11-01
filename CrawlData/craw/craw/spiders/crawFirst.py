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
  content = response.xpath('string(//*[@id="chapter"]/div)').extract()
  strName = ''.join(name)
  strContent = '|'.join(content)
  nameFile = strName.lstrip()+'.txt'
  text = strContent.replace('\n','').replace('|','').encode('utf-8')
  link = response.url.encode("utf-8")
  f = open('scenicSpots/'+nameFile,'wb')
  f.write(text)
  f.close()