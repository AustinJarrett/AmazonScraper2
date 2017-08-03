# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
from scrapy.conf import settings
import logging


class MongoPipeline(object):
    def __init__(self):
		connection = MongoClient('mongodb://mturner:Harvest2016@saecomm-shard-00-00-5ilbm.mongodb.net:27017,saecomm-shard-00-01-5ilbm.mongodb.net:27017,saecomm-shard-00-02-5ilbm.mongodb.net:27017/Walmart?ssl=true&replicaSet=saecomm-shard-0&authSource=admin')
		self.db = connection['Walmart']
		
    def process_item(self, item, spider):
		self.db.Walmart_Items.insert(dict(item))
		return item