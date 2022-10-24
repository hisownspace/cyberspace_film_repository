from flask import Blueprint

film_routes = Blueprint("api/films", __name__, url_prefix="/api/films") 

@film_routes.route("")
def all_films():
  return "Hello, esteemed colleague!"