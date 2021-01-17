BOT_NAME = 'jumia'

SPIDER_MODULES = ['jumia.spiders']
NEWSPIDER_MODULE = 'jumia.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS_PER_DOMAIN = 16

COOKIES_ENABLED = True

TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'jumia.middlewares.JumiaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'jumia.middlewares.JumiaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

ITEM_PIPELINES = {
    'jumia.pipelines.ProductPipeline': 300,
    'jumia.pipelines.SellerPipeline': 300
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 2
AUTOTHROTTLE_DEBUG = True

HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

FEED_EXPORT_ENCODING = 'utf-8'
