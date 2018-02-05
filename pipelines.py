# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
class AutoprojectPipeline(object):
    def __init__(self):
        self.file=codecs.open("goods.json",'w',encoding='utf-8')
    def process_item(self,item,spider):
        for j in range(len(item['商品名称'])):
            name=item['商品名称'][j]
            price=item['商品价格'][j]
            link1=item['商品链接'][j]
            link2=item['店铺链接'][j]
            comments=item['商品评论数'][j]
            goods={"商品名称":name,"商品价格":price,'商品链接':link1,'店铺链接':link2,'商品评论数':comments}
            line=json.dumps(dict(goods),ensure_ascii=False)+'\n'
            self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()
