import requests
import time
import random
import pandas as pd
# pip install sqlalchemy==1.4.46

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['name'] = json.get('name')
    d['url_key'] = json.get('url_key')
    d['url_path'] = json.get('url_path')
    d['availability'] = json.get('availability')
    d['seller_id'] = json.get('seller_id')
    d['seller_name'] = json.get('seller_name')
    d['price'] = json.get('price')
    d['original_price'] = json.get('original_price')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['rating_average'] = json.get('rating_average')
    d['primary_category_path'] = json.get('primary_category_path')
    d['primary_category_name'] = json.get('primary_category_name')
    d['productset_id'] = json.get('productset_id')
    d['thumbnail_url'] = json.get('thumbnail_url')
    d['seller_product_id'] = json.get('seller_product_id')
    d['video_url'] = json.get('video_url')
    return d

def craw_data(link_api,page,params,headers):
    result = dict()
    params['page']=page
    response = requests.get(link_api,headers=headers, params=params)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            result = parser_product(record)
            # print(type(parser_product(record)))
    return result
