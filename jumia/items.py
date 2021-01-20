from scrapy import Item, Field


class ProductPrimaryDetails(Item):
    url = Field()
    name = Field()
    price = Field()
    discounted_price = Field()
    discount = Field()
    image_url = Field()


class ProductSecondaryDetails(Item):
    brand = Field()
    description = Field()
    customer_reviews = Field()
    ratings = Field()
    category = Field()


class ProductSellerDetails(Item):
    seller_url = Field()
    seller_name = Field()


class ProductItem(ProductPrimaryDetails, ProductSecondaryDetails, ProductSellerDetails):
    pass


class SellerItem(Item):
    seller_name = Field()
    country_of_origin = Field()
    order_fulfillment_rate = Field()
    quality_score = Field()
    seller_score = Field()
    followers = Field()
