# -*- coding: utf-8 -*-
import scrapy
import time
import random
# from pic_scrapy.pic_scrapy.items import PicScrapyItem
from ..items import PicScrapyItem
from scrapy.http.response.html import HtmlResponse


class NetbianPicSpider(scrapy.Spider):
    name = 'netbian_pic'
    allowed_domains = ['http://www.netbian.com/1280x1024/']
    start_urls = ['http://www.netbian.com/1280x1024/index_400.htm']
    num = 1

    # http://www.netbian.com/1280x1024/index_3.htm

    # "<class 'scrapy.http.response.html.HtmlResponse'>"
    def parse(self, response):
        # "//div[@class="list"]//a/@href"   //  a[starts-with(@href,'/ads')]

        # print(type(response))
        urls = response.xpath("//div[@class='list']//a[starts-with(@href,'/desk')]/@href").extract()
        # n = response.xpath("//div[@class='list']//a//img[starts-with(@alt,'cyworld')]/@alt").extract()

        # print(type(urls))
        for url in urls:
            next_url = 'http://www.netbian.com' + url
            # print('第二页' + next_url)
            # dont_filter=True 设置范围
            yield scrapy.Request(url=next_url, callback=self.getImgname, dont_filter=True)

        # print('第' + str(self.num) + '页')
        if self.num <= 30:
            self.num += 1
            href = 'http://www.netbian.com/1280x1024/index_' + str(self.num) + '.htm'
            # time.sleep(random.uniform(3, 9))
            yield scrapy.Request(url=href, callback=self.parse, dont_filter=True)

    # "<class 'scrapy.selector.unified.Selector'>"
    # scrapy.selector.unified.Selector

    # 获取图片地址
    def getImgname(self, response):
        print('*' * 30)
        download_url = response.xpath("//*[@id='main']//div[@class='pic']//img/@src").extract_first()
        download_name = response.xpath("//*[@id='main']//div[@class='pic']//img/@alt").extract_first()
        time.sleep(random.uniform(0, 2))
        imgurls = PicScrapyItem()
        if download_url != None and download_name != None:
            imgurls['urls'] = [download_url]
            imgurls['names'] = download_name
            print('下载地址:' + download_url)
            print(download_name)
            yield imgurls
