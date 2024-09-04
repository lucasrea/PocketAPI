import os

class Config:
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None
    LOG_LEVEL = 'INFO'  # Default log level
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    LOG_LEVEL = 'DEBUG'  # Debug level logging for development
    DEBUG = True

class TestingConfig(Config):
    SECRET_KEY = os.getenv('TEST_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')
    LOG_LEVEL = 'WARNING'  # Warning level logging for testing
    TESTING = True

class ProductionConfig(Config):
    SECRET_KEY = os.getenv('PROD_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
    LOG_LEVEL = 'ERROR'  # Error level logging for production

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
