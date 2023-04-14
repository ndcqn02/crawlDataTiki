import pandas as pd
from sqlalchemy import create_engine  
# pip install sqlalchemy==1.4.46
import pymysql

engine = create_engine('mysql+pymysql://root:12345@localhost/tiki')

# user = 'root'
# passw = '12345'
# host =  '127.0.0.1'
# port = 3306
# database = 'tiki'

# conn = pymysql.connect(host=host,
#                        port=port,
#                        user=user, 
#                        passwd=passw,  
#                        db=database,
#                        charset='utf8')

                

# df_product = pd.read_csv('fruits.csv') 
# print(df_product)
# # df_product.to_sql(name='test', con=conn, if_exists = 'replace', index=False)

# df_product.to_sql('test', con = engine, if_exists = 'append', chunksize = 1000)

df_product = pd.read_csv('crawled_data_ncds.csv') 
df_product.to_sql('product', con = engine, if_exists = 'replace', index=False)