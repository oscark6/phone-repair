class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///repair_shop_dev.db'
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False