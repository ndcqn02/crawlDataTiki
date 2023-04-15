from fastapi import FastAPI
import sys
import pandas as pd
sys.path.append('models')
sys.path.append('database')
sys.path.append('service')
import until_data
from connect_database import add_data_to_database
from craw_data import craw_data

app_craw = FastAPI()
@app_craw.get("/craw-product")
def craw_product():
    result = []
    for i in range(1,50):
            result.append(craw_data(until_data.link_api,i,until_data.params,until_data.headers))
    df_product = pd.DataFrame(result)
    df_product.to_csv('crawled_data_ncds.csv', index=False)
    add_data_to_database(df_product,until_data.user_name,until_data.password,until_data.database)
    return result