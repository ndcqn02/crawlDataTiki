import sys
from mysql import connector
sys.path.append("../Data_Crawling/models")
import until_data
from models_product import Product

mydb=connector.connect(user=until_data.user_name, password=until_data.password,port=until_data.port,host=until_data.host,database=until_data.database)

def craw_product(myDict):

    cursor = mydb.cursor()
    table_name = 'product'
    
    list_key = list(myDict.keys())
    columns = ", ".join(list_key)

    my_list = list(myDict.values())
    my_list = [i if i is not None else '' for i in my_list]
    values_placeholders = ", ".join(["%s"] * len(my_list))
    
    # Create a tuple of values from the values of the dictionary
    values_tuple = tuple(my_list)

    add_book = (f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholders})")

    # print(my_list[0], my_list[1], my_list[2])
    # data_book = (my_list[0], my_list[1], my_list[2])

    cursor.execute(add_book, values_tuple)


    mydb.commit() # lưu những dữ liệu chúng ta đã chèn vào DB
    cursor.close()


    return 'chen thanh cong'
    
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


if __name__ == "__main__":
    craw_product()