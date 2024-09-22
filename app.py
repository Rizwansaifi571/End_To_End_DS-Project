import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src'))

from mlproject.logger import logging

if __name__ == "__main__":
    logging.info("The execution has started")
