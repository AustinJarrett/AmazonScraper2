import scrapy
from AmazonScraper.items import WalmartscraperItem
import datetime
from pymongo import MongoClient
import ssl
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

def getUrls(url_base):   
    user = "mturner"
    password = "Harvest2016"
    socket_path = "saecomm-shard-00-00-5ilbm.mongodb.net:27017,saecomm-shard-00-01-5ilbm.mongodb.net:27017,saecomm-shard-00-02-5ilbm.mongodb.net:27017/Walmart?ssl=true&replicaSet=saecomm-shard-0&authSource=admin"
    uri = "mongodb://%s:%s@%s" % (quote_plus(user), quote_plus(password), quote_plus(socket_path))
    client = MongoClient("saecomm-shard-00-00-5ilbm.mongodb.net",
                         ssl=True)
    client.walmart.authenticate(user, password, source='admin')
    #client = MongoClient(uri)
    db = client.walmart
    urls=[]
    ids = list(db.WalmartItemsToScrape.find())
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
        if not start_urls:
            self.logger.warning('No items recieved')
        else:
            self.logger.warning('items recieved')

        title = response.xpath('//title/text()').extract_first()
        title[:-14]

        dollars = response.xpath('//span[@class="Price-characteristic"]/text()').extract_first()
        cents = response.xpath('//span[@class="Price-mantissa"]/text()').extract_first()
        price = dollars + "." + cents

        rating = response.xpath('//span[@class="ReviewsHeader-ratingPrefix"]/text()').extract_first()


        item = AmazonscraperItem()
        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['timestamp'] = getTimestamp()
        yield item
