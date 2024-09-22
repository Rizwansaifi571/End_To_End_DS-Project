import os 
import sys
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host = host, 
            user = user, 
            password = password, 
            db = db
        )
        logging.info("Connection Established", mydb)
        df = pd.read_sql_query('Select * from students', mydb)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex)

