import sys
from mysql import connector
sys.path.append("../Data_Crawling/models")
from models_product import Product
import until_data
mydb=connector.connect(user=until_data.user_name, password=until_data.password,port=until_data.port,host=until_data.host,database=until_data.database)
def craw_product(product: Product()):
    cursor = mydb.cursor()
    my_dict = product.__dict__
    list_key = list(my_dict.keys())
    columns = ", ".join(list_key)    
    my_list = list(my_dict.values())
    values_placeholders = ", ".join(["%s"] * len(my_list))
    values_tuple = tuple(my_list)
    query =  (f"INSERT INTO product ({columns})  VALUES ({values_placeholders})")
    cursor.execute(query,values_tuple)
    mydb.commit()
    result = cursor.fetchall()
    return result
    
def search_product(product_name:str):
    cursor = mydb.cursor()
    query = "SELECT * FROM product WHERE product_name= %s"
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

    my_dict = product.__dict__
    print(my_dict)
    cursor.execute(query,my_dict.values())
    mydb.commit()
    cursor.close()
    # result = cursor.fetchall()
    return cursor.fetchall()
    
def search_product(product_name):
    cursor = mydb.cursor()
    query = "SELECT * FROM product WHERE name LIKE %s"
    value = (f"%{product_name}%",)
    cursor.execute(query, value)
    results = cursor.fetchall()
    return results
def update_product(product):
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