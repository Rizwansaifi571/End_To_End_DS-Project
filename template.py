import os
from pathlib import Path
import logging

# Setting up basic logging configuration to display log messages with a minimum level of INFO.
logging.basicConfig(level=logging.INFO)

# Defining the project name that will be used in creating the directory structure.
project_name = 'mlproject'

# List of file paths to be created in the project. It includes Python modules, scripts, and configuration files.
list_of_file = [
    f"src/{project_name}/__init__.py",  # Package initializer for 'mlproject'
    f"src/{project_name}/components/__init__.py",  # Package initializer for 'components'
    f"src/{project_name}/components/data_ingestion.py",  # Module for data ingestion component
    f"src/{project_name}/components/data_transformation.py",  # Module for data transformation component
    f"src/{project_name}/components/model_trainer.py",  # Module for training models
    f"src/{project_name}/components/model_monitering.py",  # Module for model monitoring
    f"src/{project_name}/pipelines/__init__.py",  # Package initializer for 'pipelines'
    f"src/{project_name}/pipelines/training_pipeline.py",  # Module for training pipeline
    f"src/{project_name}/pipelines/prediction_pipeline.py",  # Module for prediction pipeline
    f"src/{project_name}/exception.py",  # Custom exceptions
    f"src/{project_name}/logger.py",  # Logger module
    f"src/{project_name}/utils.py",  # Utility functions module
    "app.py",  # Main application script
    "Dockerfile",  # Docker configuration file
    "requirements.txt",  # Dependencies for the project
    "setup.py",  # Setup configuration for packaging the project
    "main.py",  # Entry point for the project
]

# Looping through the list of files to create the necessary directories and empty files.
for filepath in list_of_file:
    # Convert the string path into a Path object, which works across different operating systems.
    filepath = Path(filepath)
    
    # Split the filepath into directory and filename.
    filedir, filename = os.path.split(filepath)

    # If the directory (filedir) is not an empty string, create it if it doesn't already exist.
    if filedir != "":
        # Create the directory and any intermediate directories as needed.
        os.makedirs(filedir, exist_ok=True)
        # Log a message indicating that the directory is being created.
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create the file if it does not exist or if it's an empty file.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode ('w') to create an empty file.
        with open(filepath, 'w') as f:
            pass  # No content is written to the file, leaving it empty.
        # Log a message indicating the creation of the empty file.
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and is not empty, log that it already exists.
    else:
        logging.info(f"{filename} already exists")
