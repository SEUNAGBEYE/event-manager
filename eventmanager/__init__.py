from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(env):
  app = Flask(__name__)
  app.config.from_object(config[env])
  db.init_app(app)
  from eventmanager.user.views import user as user_blueprint
  app.register_blueprint(user_blueprint, url_prefix='/users')

  return app
  