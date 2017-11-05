from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from btou.items import ItcastItem
class ItcastSpider(CrawlSpider):
   name = "itcast"
   siteUrl = 'xx'
    

   def __init__(self,category=None,*args,**kwargs):
    print("not want to print me ????")
    print(category)
    self.rules = [Rule(LinkExtractor(allow=r"/%s" %category),'parse_item')]
    print(self.siteUrl)
    super(ItcastSpider,self).__init__(*args,**kwargs)
    #rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]
    self.start_urls = ["http://www.itcast.cn/","http://www.520it.com"]
    print("guess who print first")
    #self.rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]
   print("run me first please!!")   
   def parse_item(self,response):
	 
	 title = response.xpath("//title")
	 items = ItcastItem()
	 items['title'] = title.xpath('text()').extract()

	 h1 = response.xpath("//meta[contains(@name,'keywords')]/@content")
	 items['h1'] = h1.extract()

	 return items
