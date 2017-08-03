import scrapy
from AmazonScraper.items import WalmartscraperItem
import datetime
from pymongo import MongoClient
import ssl


def getUrls(url_base):   
    user = "mturner"
    password = "Harvest2016"
    client = MongoClient('mongodb://mturner:Harvest2016@saecomm-shard-00-00-5ilbm.mongodb.net:27017,saecomm-shard-00-01-5ilbm.mongodb.net:27017,saecomm-shard-00-02-5ilbm.mongodb.net:27017/Walmart?ssl=true&replicaSet=saecomm-shard-0&authSource=admin')
    #client = MongoClient(uri)
    db = client['Walmart']
    urls=[]
    ids = db.WalmartItemsToScrape.find()
    for id in ids:
        urls.append(url_base + id['id'])
    return urls

def getTimestamp():
	return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class AmazonscraperSpider(scrapy.Spider):
    name = "walmartscraper"
    allowed_domains = ['walmart.com']
    url_base = 'https://www.walmart.com/ip/'

    start_urls = getUrls(url_base)

    def parse(self, response):
        id = response.xpath('//a[@class="hide-content-m"]/@href').extract_first()
        id = id[18:]

        title = response.xpath('//title/text()').extract_first()
        title = title[:-14]

        dollars = response.xpath('//span[@class="Price-characteristic"]/text()').extract_first()
        cents = response.xpath('//span[@class="Price-mantissa"]/text()').extract_first()
        price = dollars + "." + cents

        rating = response.xpath('//span[@class="ReviewsHeader-ratingPrefix"]/text()').extract_first()


        item = WalmartscraperItem()
        item['id'] = id
        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['timestamp'] = getTimestamp()
        yield item
