import os
from dotenv import load_dotenv
import json
import logging.config
import pathlib

load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')

# Configura Logging
config_file = pathlib.Path("logging_config.json")
with open(config_file) as f_in:
    config = json.load(f_in)

logging.basicConfig(level="INFO")
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)