import sys
import datetime
import time
sys.path.append('Data_Crawling/models')
sys.path.append('Data_Crawling/service')
import craw_data 
import until_data
from models_product import *
from fastapi import FastAPI, HTTPException

app_craw = FastAPI()

@app_craw.post("/craw-product")
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

@app_craw.get("/search/{category_name}")
async def search_data(category_name:str):
    if(HTTPException(200)):
        result = craw_data.search_data(category_name)
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


@app_craw.put("/update_data")
async def update_product(product : Product):
    try:
        result = craw_data.update_product(product)
        return {
                "status" : "200",
                "message": "User updated",
                "data" : result
                }  
    except Exception as e:
        return str(e)


@app_craw.delete("/delete_data/{product_id}")
async def delete_data(product_id):
    try:
        craw_data.delete_product(product_id)
        return {
            "status": "200",
            "message": "Data has been deleted successfully!",
            }
    except Exception as e:
        return {"error": str(e)}
@app_craw.get("/product")
async def getAll():
    try:
        result = craw_data.getAll()
        return  {
                "status" : "200",
                "message": "get all product",
                "data" : result
                }  
    except Exception as e:
        {
                "status" : "500",
                "message": "err"+str(e),
                } 
@app_craw.post("/insert_product")
async def inset_product(product: Product):
    try:
        result = craw_data.insert_product(product)
        return {
            "status" : "200",
            "message" : "insert product",
            "data" : result
        }
    except Exception as e:
        return {"err" : e}
