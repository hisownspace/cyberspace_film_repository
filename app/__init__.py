from flask import Flask, jsonify, url_for, render_template

from .config import Configuration as Config
from .api.actor_routes import actor_routes
from .api.film_routes import film_routes

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(actor_routes, url_prefix="/api/actors")
app.register_blueprint(film_routes) 

@app.route("/")
def index():
  """This is the splash page for the Cyberspace Film Repository"""
  return render_template("index.html")
  return "Welcome to the Cyberspace Film Repository!"

@app.route("/api/help")
def help():
  """This route provides the backend routes!"""
  func_list = {}
  for rule in app.url_map.iter_rules():
    if rule.endpoint != 'static':
      func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
  return jsonify(func_list)
