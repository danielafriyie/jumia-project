from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from jumia.items import ProductPrimaryDetails


class SamsungPriceMonitorSpider(CrawlSpider):
    name = 'samsung_price_monitor'
    allowed_domains = ['jumia.com.gh']
    start_urls = ['https://www.jumia.com.gh/mobile-phones/samsung']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=("//div[@class='-paxs row _no-g _4cl-3cm-shs']/article/a",)),
            callback='parse_item',
            follow=True
        ),
        # Rule(LinkExtractor(restrict_xpaths=("//a[@aria-label='Next Page']",)), follow=True)
    )

    def parse_item(self, response):
        samsung_phone = ProductPrimaryDetails()

        samsung_phone['url'] = response.url
        samsung_phone['name'] = response.xpath("//h1[@class='-fs20 -pts -pbxs']/text()").get()
        samsung_phone['price'] = ''.join(response.xpath("(//span[@dir='ltr'])[2]/text()").re(r"\d+"))
        samsung_phone['discounted_price'] = ''.join(response.xpath("(//span[@dir='ltr'])[1]/text()").re(r"\d+"))
        samsung_phone['discount'] = ''.join(response.xpath("//span[@class='tag _dsct _dyn -mls']/text()").re(r"\d+"))
        samsung_phone['image_url'] = response.xpath("(//a[@class='itm']/img)[1]/@data-src").get()

        yield samsung_phone
