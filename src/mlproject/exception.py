import sys
from mlproject.logger import logging

def error_message_details(error, error_details: sys):
    # Extract traceback details
    _, _, exc_tb = error_details.exc_info()
    
    # Get the filename and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Construct an error message
    error_message = f"Error occurred in Python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        # Call the function to get formatted error message
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self) -> str:
        return self.error_message
