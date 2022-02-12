# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class WyijobsPipeline:
    def __init__(self):
        self.file = open('wyjobs.json', 'w')

    def process_item(self, item, spider):
        item = dict(item)
        json_str = json.dumps(item, ensure_ascii=False) + '\n'
        self.file.write(json_str)
        return item

    def __del__(self):
        self.file.close()
