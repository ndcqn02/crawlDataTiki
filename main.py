import sys
import pandas as pd
sys.path.append('Data_Crawling/models')
sys.path.append('Data_Crawling/service')
import craw_data 
import until_data
import schedule
from models_product import *
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

@app_craw.get("/search/{product_name}")
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
# @app_craw.get("/craw_by_time")
# async def craw_by_time(time_run : Time_run()):
#     craw= schedule.every().day.at("{time_run.hour}:{minute}:{second}").do(craw_data.craw_data(until_data.link_api,
#                 until_data.params, until_data.headers))
#     schedule.cancel_job(craw)

