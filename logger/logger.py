import logging.config
import os


class Logger:

    def __init__(self):
        self.logging_path = os.path.join(os.path.dirname(__file__), 'logger.conf')
        logging.config.fileConfig(self.logging_path)

    def log_error(self, message):
        logging.getLogger('error').error(message, exc_info=True)
