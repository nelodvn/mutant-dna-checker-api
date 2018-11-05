import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = 'my_precious'
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    MONGO_URI = os.getenv('MONGO_URI')


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    MONGO_URI = os.getenv('MONGO_URI_TEST')
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SECRET_KEY = '-6hu0sr=qd*t4*&osv*d=4wjg3n#*0pkl#=(!va$8%#m6+0ekm'
    pass
