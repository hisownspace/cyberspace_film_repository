from flask import Flask

from .config import Configuration as Config
from .api.actor_routes import actor_routes

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(actor_routes, url_prefix="/api/actors")

@app.route("/")
def index():
  return "Hello!"
