from pydantic import BaseModel

class Product(BaseModel):
    id =0
    sku = ''
    name = ''
    url_key =''
    url_path =''
    availability = 0
    seller_id = 0
    seller_name =''
    price = 0
    original_priceid = 0
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
