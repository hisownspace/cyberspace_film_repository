import os


class Configuration:
  FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
