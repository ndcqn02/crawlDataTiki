
import sys
import pandas as pd
sys.path.append('models')
sys.path.append('database')
sys.path.append('service')
import mysql.connector
from craw_data import craw_data
from connect_database import add_data_to_database
import until_data
from fastapi import FastAPI

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="tiki"
)


app_craw = FastAPI()


@app_craw.get("/craw-product")
def craw_product():
    result = []
    for i in range(1, 50):
        result.append(craw_data(until_data.link_api, i,
                      until_data.params, until_data.headers))
    df_product = pd.DataFrame(result)
    df_product.to_csv('crawled_data_ncds.csv', index=False)
    add_data_to_database(df_product, until_data.user_name,
                         until_data.password, until_data.database)
    return result


@app_craw.get("/search")
async def search_data(product_name: str):
    cursor = mydb.cursor()
    query = "SELECT * FROM product WHERE name LIKE %s"
    value = (f"%{product_name}%",)
    cursor.execute(query, value)
#     print(type(cursor.fetchall()))
    results = cursor.fetchall()
    return {"data": results}


@app_craw.put("/update_data/{product_id}")
def update_product(product_id: int, name: str):
    cursor = mydb.cursor()
    query = "UPDATE product SET name=%s WHERE id=%s"
    cursor.execute(query, (name, product_id))
    mydb.commit()
    cursor.close()
    return {"message": "User updated"}


@app_craw.delete("/delete_data/{product_id}")
def delete_data(product_id: int):
    try:
        cursor = mydb.cursor()
        query = "DELETE FROM product WHERE id=%s"
        cursor.execute(query, (product_id,))
        mydb.commit()
        cursor.close()
        return {"message": "Data has been deleted successfully!"}
    except Exception as e:
        return {"error": str(e)}
