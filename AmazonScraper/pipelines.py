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
		connection = MongoClient(settings['MONGODB_HOST'])
		self.db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]
		
    def process_item(self, item, spider):
		collection = self.db[type(item).__name__.lower()]
		logging.info(collection.insert(dict(item)))
		return item