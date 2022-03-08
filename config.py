import os
class Config:
    '''
    General configuration parent class
    '''
       # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:ruth@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ="ruthjmimo@gmail.com"
    MAIL_PASSWORD ="34292090"
    SECRET_KEY = os.environ.get("SECRET_KEY")
 

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:ruth@localhost/pitches'
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:ruth@localhost/pitches'
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}

