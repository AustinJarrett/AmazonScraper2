import scrapy
from AmazonScraper.items import AmazonscraperItem
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
    name = "amazonscraper"
    allowed_domains = ['amazon.com']
    url_base = 'https://www.amazon.com/dp/'
    start_urls = {"https://www.amazon.com/dp/B003QA4642"}

#    start_urls = getUrls(url_base)

    def parse(self, response):
        title = response.xpath('//title/text()').extract()
        title[11:]

        price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract()

        rating = response.xpath('//span[@class="arp-rating-out-of-text"]/text()').extract()
        rating[:3]

        ranking = response.xpath('//table[@class="a-keyvalue prodDetTable"]/tr/td/span/span/text()').extract()
        ranking[:(ranking.find('(')-1)]

        rank = ranking[1:(ranking.find('i')-1)]
        category = ranking[(ranking.find('n')+2):]

        print(title)
        print(price)
        print(rating)
        print(rank)
        print(category)

        item = AmazonscraperItem()
        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['ranking'] = rank
        item['category'] = category
        item['timestamp'] = getTimestamp()
        yield item