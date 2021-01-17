from scrapy import Spider, Request

from jumia.items import ProductItem, SellerItem


class MobilePhonesSpider(Spider):
    name = 'mobile_phones'
    allowed_domains = ['www.jumia.com.gh']
    start_urls = [
        'https://www.jumia.com.gh/mobile-phones/'
    ]

    def parse(self, response, **kwargs):
        phones = response.xpath("//a[@class='core']")
        for phone in phones:
            product_link = phone.xpath(".//@href").get()
            if product_link:
                yield response.follow(url=product_link, callback=self.parse_phone_details)

        next_page = response.xpath("//a[@aria-label='Next Page']/@href").get()
        if next_page:
            yield Request(response.urljoin(next_page), self.parse)

    def parse_phone_details(self, response):
        product = ProductItem()
        product['url'] = response.url
        product['name'] = response.xpath("//h1[@class='-fs20 -pts -pbxs']/text()").get()
        product['brand'] = response.xpath("(//div[@class='-fs14 -pvxs']/a/text())[1]").get()
        product['description'] = response.xpath("//div[@class='markup -mhm -pvl -oxa -sc']/descendant::text()").getall()
        product['price'] = response.xpath("(//span[@dir='ltr'])[2]/text()").get()
        product['discounted_price'] = response.xpath("(//span[@dir='ltr'])[1]/text()").get()
        product['discount'] = response.xpath("//span[@class='tag _dsct _dyn -mls']/text()").get()
        product['image_url'] = response.xpath("(//a[@class='itm']/img)[1]/@data-src").get()
        product['customer_reviews'] = response.xpath("//article[@class='-fs14 -pvs -hr _bet']/p/text()").getall()
        product['ratings'] = response.xpath("//div[@class='-fs29 -yl5 -pvxs']/span/text()").get()
        product['category'] = 'mobile phones',
        seller_link = response.xpath("//div[@class='-pts']/section/a/@href").get()
        seller_name = response.xpath("//div[@class='-pts']/section/div/p/text()").get()
        product['seller_url'] = response.urljoin(seller_link)
        product['seller_name'] = seller_name

        yield product
        yield response.follow(url=seller_link, callback=self.parse_seller_link, meta={'seller_name': seller_name})

    def parse_seller_link(self, response):
        seller_name = response.request.meta['seller_name']
        link = response.xpath("//a[@class='btn _def _ti -mla -fsh0']/@href").get()
        yield response.follow(url=link, callback=self.parse_seller_details, meta={'seller_name': seller_name})

    def parse_seller_details(self, response):
        seller = SellerItem()
        seller['seller_name'] = response.request.meta['seller_name']
        seller['country_of_origin'] = response.xpath("//div[@class='-df -i-ctr -plm -fs16']/span/text()").get()
        seller['order_fulfillment_rate'] = response.xpath(
            "(//div[@class='-df -i-ctr -pts -phm']/p/span/text())[1]"
        ).get()
        seller['quality_score'] = response.xpath("(//div[@class='-df -i-ctr -pts -phm']/p/span/text())[2]").get()
        seller['seller_score'] = response.xpath("//p[@class='-fs16 -pbs -phm']/span/text()").get()
        seller['followers'] = response.xpath("(//div[@class='-fs16 -df -i-ctr -mla -phm']/p/span/text())[1]").get()

        yield seller
