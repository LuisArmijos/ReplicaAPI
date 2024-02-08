from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    debug = True

config = {
    'development': DevelopmentConfig
}