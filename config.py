from env import env

class Config(object):
  DEBUG = False
  TESTING = False
  DATABASE = {
    'user': env['DATABASE_USER'],
    'password': env['DATABASE_PASSWORD'],
    'database': env['DATABASE'],
    'host': 'localhost',
    'port': '5432',
  }
  SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s:\
  %(port)s/%(database)s' % DATABASE
  SQLALCHEMY_TRACK_MODIFICATIONS = False 

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  Config.DATABASE['database'] = env['DATABASE_TEST']
  DEBUG = True

class TestingConfig(Config):
  Config.DATABASE['database'] = env['DATABASE']
  TESTING = True

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'testing': ProductionConfig
}