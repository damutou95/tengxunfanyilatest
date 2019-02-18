# -*- coding: utf-8 -*-
import scrapy
from tengxunfanyi.items import TengxunfanyiItem
from tengxunfanyi import settings
from scrapy import FormRequest
import json
import execjs
import re
from scrapy import Request

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    #allowed_domains = ['fanyi.qq.com']
    start_urls = ['https://fanyi.qq.com/']
    headers = settings.HEADERS
    def get_uuid(self):
        jsCode = """function uuid() {
        var r = "" + (new Date).getTime()
        return r
    }"""
        jsPlus = execjs.compile(jsCode)
        return jsPlus.call('uuid', )

    def start_requests(self):
        with open(settings.FILEPATH, 'r') as f:
            kws = f.readlines()
        for kw in kws:
            yield Request(url=self.start_urls[0], callback=self.parse, headers=self.headers, dont_filter=True, meta={'kw': kw.strip(), 'tag': 0})

    def parse(self, response):
        formdata = {
            'source': 'auto',
            'target': 'en',
            'qtv': re.findall('qtv = "(.*?)";', response.text)[0],
            'qtk': re.findall('qtk = "(.*?)";', response.text)[0],
            'sessionUuid': 'translate_uuid' + str(self.get_uuid()),
            'sourceText': response.meta['kw']
        }
        # 注意这里不要去重因为每次请求都是用的同一个网站
        url = 'https://fanyi.qq.com/api/translate'
        yield FormRequest(url=url, callback=self.parseItem, formdata=formdata, dont_filter=True, meta={'tag': 0})


    def parseItem(self, response):
        item = TengxunfanyiItem()
        results = json.loads(response.text)
        item['original'] = results['translate']['records'][0]['sourceText']
        item['translation'] = results['translate']['records'][0]['targetText']
        return item
