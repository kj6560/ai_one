#!/usr/bin/python3
import sys
import logging
import site

# Add the virtual environment site-packages
site.addsitedir('/var/www/shiwkesh/nudity/venv/lib/python3.10/site-packages')

# Configure logging
logging.basicConfig(stream=sys.stderr)

# Add project directory to sys.path
sys.path.insert(0, "/var/www/shiwkesh/nudity/")

# Import and initialize Flask app
from FlaskApp import app as application
application.secret_key = 'ai_one_keshav'