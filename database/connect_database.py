from sqlalchemy import create_engine

def add_data_to_database(data_frame,user_name,password,database_name):
    sql='mysql+pymysql://{}:{}@localhost/{}'
    try:
        engine = create_engine(sql.format(user_name,password,database_name))
        data_frame.to_sql('product', con = engine, if_exists = 'replace', index=False)
        print('ghi du lieu thanh cong')
    except:
        print("error:")