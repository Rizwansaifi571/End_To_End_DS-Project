import logging
import os
from datetime import datetime

# Generate a log file name with the current date and time to ensure unique log files.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path for storing log files under the "logs" folder within the current working directory.
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the directory for log files exists. If it doesn't exist, create it.
os.makedirs(log_path, exist_ok=True)

# Define the full path for the log file, including the directory and the log file name.
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging module.
logging.basicConfig(
    # Set the file where the log output will be written.
    filename=LOG_FILE_PATH, 
    
    # Define the format for log messages.
    # %(asctime)s: Timestamp when the log entry is created.
    # %(lineno)d: Line number in the source code where the log entry was created.
    # %(name)s: Logger name.
    # %(levelname)s: Log level (e.g., INFO, DEBUG, ERROR).
    # %(message)s: The actual log message.
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    
    # Set the minimum logging level. INFO level logs informational messages along with warnings and errors.
    level=logging.INFO,
)
