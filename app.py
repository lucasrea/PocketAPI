import os
from dotenv import load_dotenv
from flask import Flask
import logging
from config import config

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Determine the configuration to use
config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

# Set up logging
log_level = app.config.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger(__name__)

# logger.info('Flask application started')
# logger.debug('Debugging is active')
# logger.warning('This is a warning')

from routes import *

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
