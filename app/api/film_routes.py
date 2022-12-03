import json
from flask import Blueprint, request

from app.models import db, Film, Actor
from app.forms.FilmForm import FilmForm

film_routes = Blueprint("api/films", __name__, url_prefix="/api/films") 

@film_routes.route("/")
def all_films():
  films = Film.query.all()
  return { film.id: film.to_dict() for film in films }, 200

@film_routes.route("/<int:id>")
def one_film(id):
  film = Film.query.get(id)
  print(film.to_dict())
  try:
    if not film:
      return { "errors": "Film not found"}, 404
    return film.to_dict(), 200
  except Exception as e:
    return { "errors": str(e) }, 500

@film_routes.route("/count")
def film_count():
  return { "totalFilms": Film.query.count() }, 200

@film_routes.route("/", methods=["POST"])
def add_film():
  form = FilmForm()
  form["csrf_token"].data = request.cookies["csrf_token"]
  
  if form.validate_on_submit():
    params = {
      "title": form.data["title"],
      "year": form.data["year"],
      "plot": form.data["plot"],
      "photo_url": form.data["photo_url"],
      "genre_id": form.data["genre_id"]
    }
    film = Film(**params)
    
    cast = json.loads(form.data["castIds"])

    for id in cast:
      actor = Actor.query.get(id)
      film.cast.append(actor)
    
    try:
      db.session.add(film)
      db.session.commit()
    except Exception as e:
      return { "errors": str(e) }
    