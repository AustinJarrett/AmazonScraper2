import scrapy
from AmazonScraper.items import WalmartscraperItem
import datetime
#import pymssql 

#def getUrls(url_base):
#    conn = pymssql.connect("Data Source=buffalo;User id=pidMT; Password=Mawu4230; Connection Timeout=5000")
#    cursor = conn.cursor()
#    cursor.execute("USE [eCommerce] SELECT [ASIN] FROM [eCommerce].[dbo].[Amazon_ASINs]")
#    urls=[]
#    for row in cursor:
#        urls.append(url_base + row[0])
#    return urls

def getTimestamp():
	return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class AmazonscraperSpider(scrapy.Spider):
    name = "walmartscraper"
    allowed_domains = ['walmart.com']
    url_base = 'https://www.walmart.com/ip/'

#    start_urls = getUrls(url_base)

    def parse(self, response):
        title = response.xpath('//title/text()').extract()
        title[:-14]

        dollars = response.xpath('//span[@class="Price-characteristic"]/text()').extract_first()
        cents = response.xpath('//span[@class="Price-mantissa"]/text()').extract_first()
        price = dollars + "." + cents

        rating = response.xpath('//span[@class="ReviewsHeader-ratingPrefix"]/text()').extract()


        item = AmazonscraperItem()
        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['timestamp'] = getTimestamp()
        yield item
