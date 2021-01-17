from scrapy import Item, Field


class ProductItem(Item):
    url = Field()
    name = Field()
    brand = Field()
    description = Field()
    price = Field()
    discounted_price = Field()
    discount = Field()
    image_url = Field()
    customer_reviews = Field()
    ratings = Field()
    category = Field()
    seller_url = Field()
    seller_name = Field()


class SellerItem(Item):
    seller_name = Field()
    country_of_origin = Field()
    order_fulfillment_rate = Field()
    quality_score = Field()
    seller_score = Field()
    followers = Field()
