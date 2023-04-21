from pydantic import BaseModel

class Product(BaseModel):
    id_product =0
    sku = ''
    product_name = ''
    url_key =''
    url_path =''
    availability = 0
    seller_id = 0
    seller_name =''
    price = 0
    original_price = 0
    discount = 0
    discount_rate = 0
    review_count = 0
    rating_average = 0
    primary_category_path =''
    primary_category_name =''
    productset_id = 0
    seller_product_id = 0
    thumbnail_url =''
    video_url =''
class Time_run(BaseModel):
    hour = 0
    minute = 0
    second = 0