from flask import Blueprint
from app.models.films import Film

film_routes = Blueprint("api/films", __name__, url_prefix="/api/films") 

@film_routes.route("/")
def all_films():
  films = Film.query.all()
  return { film.id: film.to_dict() for film in films }, 200

@film_routes.route("/<int:id>")
def one_film(id):
  film = Film.query.get(id)
  return film.to_dict(), 200

@film_routes.route("/count")
def film_count():
  return { "totalFilms": Film.query.count() }, 200