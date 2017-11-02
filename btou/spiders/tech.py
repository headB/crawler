from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from btou.items import BtouItem
class TechSpider(CrawlSpider):
   name = "tech"
   allowed_domains = ["520it.com"]
   start_urls = ["http://520it.com/"]
   rules = [Rule(LinkExtractor(allow=r"/special/*"),'parse_item')]
 
   def parse_item(self,response):
     sites = response.xpath('//h1')
     items = []
     content = []
     for site in sites:
       content.append(''.join(site.xpath('text()').extract()))
     item = BtouItem()
     item['name'] = response.url
     #item['desc'] = ''.join(content)
     items.append(item)
     return items
