from scrapy import cmdline
from scrapy.pipelines.images import  ImagesPipeline
cmdline.execute('scrapy crawl netbian_pic'.split())