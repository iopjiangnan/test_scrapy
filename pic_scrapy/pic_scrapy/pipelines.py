# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import re
# from scrapy.pipelines.images import ImagesPipeline

import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagesrenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['urls']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(image_url, meta={'name': item['names']})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        image_guid = request.meta['name']
        # 接收上面meta传递过来的图片名称
        # name = request.meta['name']
        # # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        # name = re.sub(r'[？\\*|“<>:/]', '', name)
        # # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        # filename = u'{0}/{1}'.format(name, image_guid)
        return 'full/%s.jpg' % (image_guid)

# class PicScrapyPipeline(object):
#     def __init__(self):
#         self.file = open('qsbk.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫开始了...')
#         pass
#
#     def process_item(self, item, spider):
#         # 这里需要把item转换字典
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.file.write(item_json + '\n')
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()
#         print('爬虫结束了...')
#         pass
