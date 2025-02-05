#!/usr/bin/python3
import sys
import logging
import os


# Configure logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# Add project directory to sys.path
sys.path.insert(0, "/var/www/shiwkesh/nudity/")

# Import and initialize Flask app
try:
    import app as application
except ImportError as e:
    logging.error(f"Failed to import Flask app: {e}")
    raise

# Set secret key securely
application.secret_key = os.getenv("SECRET_KEY", "default_fallback_key")
