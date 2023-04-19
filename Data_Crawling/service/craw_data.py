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
def parser_product(json):
    product = Product(
        id = json.get('id')
    )
    product.id = json.get('id')
    product.sku = json.get('sku')
    product.name = json.get('name')
    product.url_key = json.get('url_key')
    product.url_path = json.get('url_path')
    product.availability = json.get('availability')
    product.seller_id = json.get('seller_id')
    product.seller_name= json.get('seller_name')
    product.price = json.get('price')
    product.original_priceid = json.get('original_price')
    product.discount = json.get('discount')
    product.discount_rate = json.get('discount_rate')
    product.rating_average = json.get('review_count')
    product.rating_average = json.get('rating_average')
    product.primary_category_path = json.get('primary_category_path')
    product.primary_category_name = json.get('primary_category_name')
    product.productset_id= json.get('productset_id')
    product.seller_product_id = json.get('seller_product_id')
    product.thumbnail_url = json.get('thumbnail_url')
    product.video_url = json.get('video_url')
    return product
product = Product()
def craw_data(link_api,page,params,headers):
    params['page']=page
    result = Product()
    response = requests.get(link_api,headers=headers, params=params)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            result = parser_product(record)
            database_api.update_data(result)
    return result
def search_data(product_name: str):
        return database_api.search_product(product_name)
def update_product(product : Product):
        return database_api.update_product(product)
        
def delete_product(id : int):
    return database_api.delete_product(id)

