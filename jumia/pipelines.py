import sqlite3 as sq
import os
import logging

from scrapy.exceptions import DropItem

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, 'jumia.sqlite3')

try:
    os.remove(db_path)
except OSError:
    pass

connection = sq.connect(db_path)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        url TEXT,
        name TEXT,
        brand VARCHAR(250),
        description TEXT,
        price VARCHAR(20),
        discounted_price VARCHAR(20),
        discount VARCHAR(20),
        image_url TEXT,
        customer_reviews TEXT,
        ratings VARCHAR(20),
        category VARCHAR(150),
        seller_url TEXT,
        seller_name VARCHAR(250)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS seller (
        seller_name VARCHAR(250),
        country_of_origin VARCHAR(150),
        order_fulfillment_rate VARCHAR(20),
        quality_score VARCHAR(20),
        seller_score VARCHAR(20),
        followers VARCHAR(20)
    );
""")

connection.commit()


def insert(table, columns=(), values=()):
    if len(columns) != len(values):
        raise ValueError(f"columns length {len(columns)} != values length {len(values)}")

    anonymous_columns = ','.join('?' * len(columns))
    cursor.execute(
        f"INSERT INTO {table} {columns} VALUES ({anonymous_columns});",
        tuple(data if isinstance(data, str) else str(data) for data in values)
    )
    connection.commit()


class ProductPipeline:
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'ProductItem':
            insert(
                table='product',
                columns=(
                    'url',
                    'name',
                    'brand',
                    'description',
                    'price',
                    'discounted_price',
                    'discount',
                    'image_url',
                    'customer_reviews',
                    'ratings',
                    'category',
                    'seller_url',
                    'seller_name'
                ),
                values=(
                    item['url'],
                    item['name'],
                    item['brand'],
                    item['description'],
                    item['price'],
                    item['discounted_price'],
                    item['discount'],
                    item['image_url'],
                    item['customer_reviews'],
                    item['ratings'],
                    item['category'],
                    item['seller_url'],
                    item['seller_name']
                )
            )
        return item


class SellerPipeline:
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'SellerItem':
            insert(
                table='seller',
                columns=(
                    'seller_name',
                    'country_of_origin',
                    'order_fulfillment_rate',
                    'quality_score',
                    'seller_score',
                    'followers',
                ),
                values=(
                    item['seller_name'],
                    item['country_of_origin'],
                    item['order_fulfillment_rate'],
                    item['quality_score'],
                    item['seller_score'],
                    item['followers']
                )
            )
        return item


class SamsungPriceMonitorPipeline:
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'ProductPrimaryDetails':
            if item.get('discount'):
                if float(item.get('discount')) > 15:
                    return item
            raise DropItem(f"Discount is less than 15% {item}")
