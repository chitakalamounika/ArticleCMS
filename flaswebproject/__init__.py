import logging
from flask import Flask

app = Flask(__name__)
app.config.from_object("FlaskWebProject.config")  # load config from config.py

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Flask app started and logging is configured")
