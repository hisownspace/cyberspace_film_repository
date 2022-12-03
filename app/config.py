import os


class Configuration:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_URL")
  SQLALCHEMY_ECHO = False