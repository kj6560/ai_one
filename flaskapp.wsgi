#!/usr/bin/python3
import sys import logging 
import site

site.addsitedir('/var/www/shiwkesh/nudity/venv/bin/python/lib/python3.10/site-packages')
logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0,"/var/www/shiwkesh/nudity/")
from FlaskApp import app as application 
application.secret_key = 'ai_one_keshav'