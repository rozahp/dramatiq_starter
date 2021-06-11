"""Flask configuration."""

import os
import logging

# FLASK CONFIG
class Config:
    """Base config."""
    SECRET_KEY = os.urandom(32)
    WATCHER_PATH = os.environ.get('WATCHER_PATH')
    REDIS_URL = os.environ.get('REDIS_URL','localhost')
    DASHBOARD_PREFIX = os.environ.get('DASHBOARD_PREFIX','/dashboard')
    WATCHER_PATH = os.environ.get('WATCHER_PATH','/tmp')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = logging.INFO

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    LOGGING_LEVEL = logging.DEBUG

