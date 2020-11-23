import scrapy
from craw.items import CrawItem

# run in sematic_web/CrawlData/craw

crawHistory = "crawHistory"
historyUrl = "http://thegioidisan.vn/vi/c-di-tich-lich-su-van-hoa"
endPage = 14

class historySpider(scrapy.Spider):
 name = crawHistory
#  start_urls = [historyUrl]
 def start_requests(self):
  for page in range(1,endPage):
   yield self.make_requests_from_url(historyUrl+'?page=%s' %page)
 def parse(self, response):
  historyUrl = response.xpath('//*[@class="posts-wrapper"]/div/div[2]/a/@href').extract()
  for link in historyUrl:
   yield scrapy.Request(link.replace('..', 'http://thegioidisan.vn'), callback=self.saveFile)
 def saveFile(self, response):
  name = response.xpath('//*[@class="artcl-heading"]/h1/text()').extract()
  title = response.xpath('string(//*[@class="artcl-sapo"]/text())').extract()
  name = ''.join(name).strip()
  nameFile = name + '.txt'
  title = (''.join(title).strip().replace('\n','') + '\n').encode('utf-8')
  content = ''
  contentXpathArrays = response.xpath('//*[@class="artcl-content"]/p//text()').extract()
  for p in contentXpathArrays:
   content = content + ''.join(p)
  content = content.strip().encode('utf-8')
  f = open('historyRelic/'+nameFile,'wb')
  f.write(content)
  f.close()