# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class JavPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['DB_HOST'],
            settings['DB_PORT']
        )
        db = connection[settings["DB_NAME"]]
        self.all_col = db[settings["DB_COLLECTION"]]
        self.id_col = db["ids"]
    def process_item(self, item, spider):
        postItem = dict(item)
        #self.id_col.insert({"mv_id": postItem["mv_id"], "viewed" : False})
        self.all_col.insert(postItem)
        return item
