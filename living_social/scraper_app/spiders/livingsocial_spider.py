from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector 
# enables xpath request
from scrapy.contrib.loader import XPathItemLoader 
# to load data into item_fields
from scrapy.contrib.loader.processor import Join, MapCompose 
# MapCompose() for cleaning up data, Join() for joining elements

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
	""" Spider for living social SF page"""
	name = 'livingsocial'
	allowed_domains =['livingsocial.com']
	start_urls = ['https://www.livingsocial.com/cities/6-chicago']
	deals_list_xpath='//li[@dealid]'
	item_fields= {
		'title' :'.//span[@itemscope]/meta[@itemprop="name"]/@content',
		'link' : './/a/@href',
		'location' : './/a/div[@class="deal-details"]/p[@class = "location"]/text()',
		'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
		'price' : './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
		'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
	}

	def parse(self, response):
		"""
		Default callback used by Scrapy to process downloaded responses
		Testing contracts:
		@url http://www.livingsocial.com/cities/15-san-francisco
		@returns items 1
		@scrapes title link
		"""

		selector = HtmlXPathSelector(response)

		for deal in selector.xpath(self.deals_list_xpath):
			loader = XPathItemLoader(LivingSocialDeal(),selector=deal)

			# define processors
			loader.default_input_processor = MapCompose(unicode.strip) 
			# stripe out white-space of unicode strings
			loader.default_output_processor = Join() 
			# join the data together by a space

			# iterate over fields and add xpaths to the loader
			for field, xpath in self.item_fields.iteritems(): 
			# iteritems() iterate the (key,value) of items in a dictionary. There are also iterkeys() and itervalues() functions. 
				loader.add_xpath(field, xpath) 
			yield loader.load_item() 
			# yield each other and move on to the next

