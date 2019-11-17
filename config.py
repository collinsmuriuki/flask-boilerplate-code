import os 

class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = ""
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist_test"

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist"
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}