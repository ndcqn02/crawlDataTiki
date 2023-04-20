import sys
import pandas as pd
sys.path.append('Data_Crawling/models')
sys.path.append('Data_Crawling/service')
import craw_data 
import until_data
from fastapi import FastAPI, HTTPException

app_craw = FastAPI()

@app_craw.get("/craw-product")
async def craw_product():
    try:
        result = craw_data.craw_data(until_data.link_api,
                until_data.params, until_data.headers)
        return {
            "status": '200',
            'message':'success',
            'data' : result
        }
    except Exception as e:
        return {
            "status": '500',
            'message': str(e),
        }

@app_craw.get("/search")
async def search_data(product_name:str):
    if(HTTPException(200)):
        result = craw_data.search_data(product_name)
        return {
            'status' : '200',
            'message' : 'success',
            'data' : result
        }
    else:
        return{
            'status' : '400',
            'message' : 'error'
        }


@app_craw.put("/update_data/{product_id}")
async def update_product(product_id: int, name: str):
    cursor = mydb.cursor()
    query = "UPDATE product SET name=%s WHERE id=%s"
    cursor.execute(query, (name, product_id))
    mydb.commit()
    cursor.close()
    return {"message": "User updated"}


@app_craw.delete("/delete_data?product_id")
async def delete_data(product_id):
    try:
        craw_data.delete_product(id)
        return {"message": "Data has been deleted successfully!"}
    except Exception as e:
        return {"error": str(e)}
