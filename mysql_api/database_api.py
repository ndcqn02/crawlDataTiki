import sys
from mysql import connector
sys.path.append("../Data_Crawling/models")
from models_product import Product
import until_data
mydb=connector.connect(user=until_data.user_name, password=until_data.password,port=until_data.port,host=until_data.host,database=until_data.database)
print('KET NOI THANH CONG')

def find_by_id(product_id):
    cursor = mydb.cursor()
    query = "Select * FROM product WHERE id_product=%s"
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    cursor.close()
    return result
def getAll():
    cursor = mydb.cursor()
    query = "select * FROM product"
    cursor.execute(query)
    rows = cursor.fetchall()
    result = convert(rows)
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
    result = []
    try:
        cursor.execute(query,values_tuple)
        mydb.commit()
        cursor.close()
        print('insert successfully!')
    except Exception as e:
        print(e)
        mydb.rollback()
        cursor.close()
    return product
    
def search_product(category_name):
    cursor = mydb.cursor()
    query = "select * from product where  primary_category_name = %s"
    cursor.execute(query, (category_name,))
    rows = cursor.fetchall()
    results = convert(rows)
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
    mydb.commit()
    cursor.close()
    print("update success")
    return product

def delete_product(product_id):
    cursor = mydb.cursor()
    query = "DELETE FROM product WHERE id_product=%s"
    cursor.execute(query, (product_id,))
    mydb.commit()
    cursor.close()

def convert(rows):
    data= []
    for row in rows:
        product = Product()
        product.id_product = row[0]
        product.sku =row[1]
        product.product_name = row[2]
        product.url_key = row[3]
        product.url_path = row[4]
        product.availability = row[5]
        product.seller_id = row[6]
        product.seller_name= row[7]
        product.price = row[8]
        product.original_price = row[9]
        product.discount = row[10]
        product.discount_rate = row[11]
        product.review_count = row[12]
        product.rating_average = row[13]
        product.primary_category_path = row[14]
        product.primary_category_name =row[15]
        product.productset_id= row[16]
        product.seller_product_id = row[17]
        product.thumbnail_url = row[18]
        product.video_url =row[19]
        data.append(product)
    return data