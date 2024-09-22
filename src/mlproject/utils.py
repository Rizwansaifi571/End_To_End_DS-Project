import os 
import sys
from mlproject.exception import CustomException  # Custom exception for error handling
from mlproject.logger import logging  # Logger for tracking events
import pandas as pd  # Data manipulation library
from dotenv import load_dotenv  # Library to load environment variables from a .env file
import pymysql  # MySQL database adapter for Python

import pickle
import numpy as np

# Load environment variables from a .env file
load_dotenv()

# Retrieve database connection parameters from environment variables
host = os.getenv("host")  # Database host
user = os.getenv("user")  # Database user
password = os.getenv("password")  # Database password
db = os.getenv('db')  # Database name

def read_sql_data():
    logging.info("Reading SQL database started")  # Log the start of the data reading process
    try:
        # Establish connection to the MySQL database
        mydb = pymysql.connect(
            host=host, 
            user=user, 
            password=password, 
            db=db
        )
        logging.info("Connection established successfully")

        # Execute SQL query to read data from the 'students' table into a DataFrame
        df = pd.read_sql_query('SELECT * FROM students', mydb)

        # Print the first few rows of the DataFrame for verification
        print(df.head())

        return df  # Return the DataFrame containing the queried data
    
    except Exception as ex:
        # Raise a custom exception if any error occurs during the process
        raise CustomException(ex)

    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)