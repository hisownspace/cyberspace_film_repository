import os


class Configuration:
  FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_URL")
  SQLALCHEMY_ECHO = False