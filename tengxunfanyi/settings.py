# -*- coding: utf-8 -*-
import sys
# Scrapy settings for tengxunfanyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tengxunfanyi'

SPIDER_MODULES = ['tengxunfanyi.spiders']
NEWSPIDER_MODULE = 'tengxunfanyi.spiders'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DBNAME = 'tengxunfanyi'
MONGO_COLLECTIONNAME = 'fanyi'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tengxunfanyi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HEADERS = {
# 'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':  'gzip, deflate, br',
# 'Accept-Language':  'zh-CN,zh;q=0.9',
# 'Cache-Control':  'max-age=0',
# 'Connection':  'keep-alive',
# 'Cookie':  'fy_guid=f11dbcc8-40b3-43ff-a186-6cbee945ff8b; ts_refer=www.baidu.com/link; pgv_pvid=6649653614; ts_uid=3486231084; gr_user_id=a4bbef5c-a02b-48b6-877b-008eb0d29f90; grwng_uid=9543266b-daf4-4c50-a991-c5b2147c8f54; openCount=100; pgv_info=ssid=s2877124276; qtv=54e1fa1844bb553c; qtk=I3FVMWqCeGAI3sAXg/xcx2yzjr1rJhwhs3Uyux/KTXL/a2CPCfH6xHzcC/L69KPakYDYlH107GkVweDaLFGvdh/CEEfxgUfNNROOpA6RXqDYD2uwKFYZzirNLrxaOXjepNTWNmJH46N5lDUn55joLg==; 9c118ce09a6fa3f4_gr_session_id=677615bf-10e8-4e9d-8c7b-188fc7be4ed2; 8c66aca9f0d1ff2e_gr_session_id=7f5db9de-c765-4b18-9e4f-75edb04a94e2; 8c66aca9f0d1ff2e_gr_session_id_7f5db9de-c765-4b18-9e4f-75edb04a94e2=true',
# 'Host':  'fanyi.qq.com',
# 'If-None-Match':  'W/"4a6f-HjCJz4eIPHBYWooEhD1fTDwhbEk"',
# 'Referer':  'https://fanyi.qq.com/',
# 'Upgrade-Insecure-Requests':  '1',
'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tengxunfanyi.middlewares.TengxunfanyiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tengxunfanyi.middlewares.TengxunfanyiDownloaderMiddleware': 543,
    'tengxunfanyi.middlewares.HttpProxyMiddleware': 300,

 }
FILEPATH = '/home/xiyujing/文档/测试.txt'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tengxunfanyi.pipelines.TengxunfanyiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 0.5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
