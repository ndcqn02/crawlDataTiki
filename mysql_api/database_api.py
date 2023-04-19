import sys
from mysql import connector
sys.path.append("../Data_Crawling/models")
import until_data
from models_product import Product
mydb=connector.connect(user=until_data.user_name, password=until_data.password,port=until_data.port,host=until_data.host,database=until_data.database)
def craw_product(product:Product):
    cursor = mydb.cursor()
    query = "insert into product (id_product,sku,name,url_key,url_path,availability,seller_id,seller_name,price,original_priceid,discount,discount_rate,review_count,rating_average,primary_category_path,primary_category_name,productset_id,seller_product_id,thumbnail_url,video_url) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor.execute(query,product)
    result = cursor.fetchall()
    return result
    
def search_product(product_name:str):
    cursor = mydb.cursor()
    query = "SELECT * FROM product WHERE name LIKE %s"
    value = (f"%{product_name}%",)
    cursor.execute(query, value)
    results = cursor.fetchall()
    return results
def update_product(product:Product()):
    cursor = mydb.cursor()
    query = "UPDATE product SET name=%s WHERE id_product=%s"
    cursor.execute(query, (name, product_id))
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()
    return result
def delete_product(id):
    cursor = mydb.cursor()
    query = "DELETE FROM product WHERE id_product=%s"
    cursor.execute(query, product_id)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()
    return result