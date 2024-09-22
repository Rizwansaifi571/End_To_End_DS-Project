import os 
import sys
from mlproject.exception import CustomException  # Custom exception for error handling
from mlproject.logger import logging  # Logger for tracking events
import pandas as pd  # Data manipulation library
from mlproject.utils import read_sql_data  # Function to read data from SQL
from sklearn.model_selection import train_test_split  # Function to split data into training and testing sets
from dataclasses import dataclass  # Decorator for creating data classes

# Data ingestion configuration class
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path for training data
    test_data_path: str = os.path.join('artifacts', 'test.csv')  # Path for testing data
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')  # Path for raw data


class DataIngestion:
    def __init__(self):
        # Initialize the ingestion configuration
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Reading data from SQL database
            df = pd.read_csv(os.path.join('notebook/data', 'raw.csv'))
            logging.info("Reading from MySQL database")

            # Create the directory for saving the CSV files if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to a CSV file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion is complete!")

            # Return the paths of the train and test data files
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Raise a custom exception if any error occurs
            raise CustomException(e, sys)
