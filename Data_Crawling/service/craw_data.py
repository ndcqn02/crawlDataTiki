import requests
import time
import random
import pandas as pd
import importlib.util
import sys
sys.path.append("../models")
sys.path.append("./mysql_api")
from models_product import Product
import database_api
import until_data

# def parser_product(json):
#     product = Product()
#     product.id = json.get('id')
#     product.sku = json.get('sku')
#     product.name = json.get('name')
#     product.url_key = json.get('url_key')
#     product.url_path = json.get('url_path')
#     product.availability = json.get('availability')
#     product.seller_id = json.get('seller_id')
#     product.seller_name= json.get('seller_name')
#     product.price = json.get('price')
#     product.original_price = json.get('original_price')
#     product.discount = json.get('discount')
#     product.discount_rate = json.get('discount_rate')
#     product.rating_average = json.get('review_count')
#     product.rating_average = json.get('rating_average')
#     product.primary_category_path = json.get('primary_category_path')
#     product.primary_category_name = json.get('primary_category_name')
#     product.productset_id= json.get('productset_id')
#     product.seller_product_id = json.get('seller_product_id')
#     product.thumbnail_url = json.get('thumbnail_url')
#     product.video_url = json.get('video_url')
#     return product

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['name'] = json.get('name')
    d['short_description'] = json.get('short_description')
    d['price'] = json.get('price')
    d['list_price'] = json.get('list_price')
    d['price_usd'] = json.get('price_usd')
    price_usd = json.get('price_usd')
    if price_usd is None:
        d['price_usd'] = 0
    else:
        d['price_usd'] = price_usd
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['order_count'] = json.get('order_count')
    order_count = json.get('order_count')
    if order_count is None:
        d['order_count'] = 0
    else:
        d['order_count'] = order_count
    d['inventory_status'] = json.get('inventory_status')
    # d['is_visible'] = json.get('is_visible')
    # d['stock_item_qty'] = json.get('stock_item').get('qty')
    # d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
    # d['product_name'] = json.get('meta_title')
    # d['brand_id'] = json.get('brand').get('id')
    # d['brand_name'] = json.get('brand').get('name')
    return d


# product = Product()
def craw_data(link_api,page,params,headers):
    params['page']=page
    result = []
    response = requests.get(link_api,headers=headers, params=params)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            result.append(parser_product(record)) 

            # new_record = parser_product(record)
            # print(type(new_record))

            # key_list = list(new_record.keys())
            # val_list = list(new_record.values())
            # print(val_list)
 
            database_api.craw_product(parser_product(record))

    return result

def search_data(product_name: str):
        return database_api.search_product(product_name)
def update_product(product : Product):
        return database_api.update_product(product)
        
def delete_product(id : int):
    return database_api.delete_product(id)

