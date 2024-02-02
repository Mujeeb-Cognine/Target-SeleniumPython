import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('automation.log')

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Now, you can use the logger to log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
