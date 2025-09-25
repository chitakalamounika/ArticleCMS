import logging
from flask import Flask

# Create the Flask app
app = Flask(__name__)
app.config.from_object("FlaskWebProject.config")  # Load settings from config.py

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)
logger.info("Flask application initialized with logging enabled")
