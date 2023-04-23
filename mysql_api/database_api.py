import sys
from mysql import connector
sys.path.append("../Data_Crawling/models")
from models_product import Product
import until_data
mydb=connector.connect(user=until_data.user_name, password=until_data.password,port=until_data.port,host=until_data.host,database=until_data.database)

def find_by_id(product_id):
    cursor = mydb.cursor()
    query = "Select * FROM product WHERE id_product=%s"
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    cursor.close()
    return result
def getAll():
    cursor = mydb.cursor()
    query = "select * from product"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def insert_product(product: Product()):
    cursor = mydb.cursor()
    my_dict = product.__dict__
    list_key = list(my_dict.keys())
    columns = ", ".join(list_key)    
    my_list = list(my_dict.values())
    values_placeholders = ", ".join(["%s"] * len(my_list))
    values_tuple = tuple(my_list)
    query =  (f"INSERT INTO product ({columns})  VALUES ({values_placeholders})")
    try:
        cursor.execute(query,values_tuple)
        mydb.commit()
        result = cursor.fetchall()
        cursor.close()
    except:
        mydb.rollback()
        cursor.close()
    return result
    
def search_product(product_name):
    cursor = mydb.cursor()
    query = "select * from product where product_name = %s"
    cursor.execute(query, (product_name,))
    results = cursor.fetchall()
    return results
def update_product(product: Product()):
    cursor = mydb.cursor()
    query = "UPDATE product SET id_product=%s, sku=%s, product_name=%s, url_key=%s ,url_path=%s, availability=%s ,seller_id=%s, seller_name=%s,price=%s, original_price=%s, discount=%s, discount_rate=%s, review_count=%s ,rating_average=%s ,primary_category_path=%s ,primary_category_name=%s, productset_id=%s ,seller_product_id=%s ,thumbnail_url=%s ,video_url=%s  WHERE id_product=%s"
    my_dict = product.__dict__
    my_list = list(my_dict.values())
    id_product= my_list[0]
    value = my_list.append(id_product)
    values_tuple = tuple(my_list)
    values_tuple = tuple(my_list)
    result=[]
    cursor.execute(query ,values_tuple)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()
    return result

def delete_product(product_id):
    cursor = mydb.cursor()
    query = "DELETE FROM product WHERE id_product=%s"
    cursor.execute(query, (product_id,))
    mydb.commit()
    cursor.close()