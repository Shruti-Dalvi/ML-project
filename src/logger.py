import logging
import os
from datetime import datetime

# Create the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Make sure the directory exists
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Set up the logging configuration
import logging

# Set up basic logging configuration
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.INFO,  # Logging level
    format='%(asctime)s:%(levelname)s:%(message)s'
)


# Example log entry
logging.info("Logging has started")

