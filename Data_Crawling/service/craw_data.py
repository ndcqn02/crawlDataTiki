import requests
import time
import importlib.util
import sys
sys.path.append("../models")
sys.path.append("./mysql_api")
from models_product import Product
import database_api 
import until_data
def parser_product(json):
    product = Product()
    product.id_product = json.get('id')
    product.sku = json.get('sku')
    product.product_name = json.get('name')
    product.url_key = json.get('url_key')
    product.url_path = json.get('url_path')
    product.availability = json.get('availability')
    product.seller_id = json.get('seller_id')
    product.seller_name= json.get('seller_name')
    product.price = json.get('price')
    product.original_price = json.get('original_price')
    product.discount = json.get('discount')
    product.discount_rate = json.get('discount_rate')
    product.review_count = json.get('review_count')
    product.rating_average = json.get('rating_average')
    product.primary_category_path = json.get('primary_category_path')
    product.primary_category_name = json.get('primary_category_name')
    product.productset_id= json.get('productset_id')
    product.seller_product_id = json.get('seller_product_id')
    product.thumbnail_url = json.get('thumbnail_url')
    product.video_url = json.get('video_url')
    return product

def craw_data(link_api,params,headers):
    result = list()
    for i in range(1,50):
        params['page']=i
        response = requests.get(link_api,headers=headers, params=params)
        for record in response.json().get('data'):
            product = parser_product(record)
            check = database_api.find_by_id(product.id_product)
            if(check != None):
                database_api.update_product(product)
                print("update")
            else:
                database_api.insert_product(product)
                print("insert")
            result.append(product)
    # print(result)
    return result
def search_data(product_name):
        return database_api.search_product(product_name)
def update_product(product):
        return database_api.update_product(product)
        
def delete_product(product_id):
    return database_api.delete_product(product_id)
def find_by_id(product_id):
    return database_api.find_by_id(product_id)

