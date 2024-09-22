import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from mlproject.logger import logging
from mlproject.exception import CustomException

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
