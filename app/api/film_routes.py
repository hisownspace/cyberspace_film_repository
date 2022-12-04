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
  """Receives a json representing an html form, converts it to a FlaskForm,validates the form, and if valid creates a new row in the films table of the database for the movie submitted. It returns a dictionary representing that movie."""
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
    
    # dealing with db.relationship by appending to cast list
    cast = json.loads(form.data["castIds"])
    print(cast)
    for id in cast:
      print(id)
      actor = Actor.query.get(id)
      print(actor.name)
      film.cast.append(actor)
    
    try:
      db.session.add(film)
      db.session.commit()
      return film.to_dict()
    except Exception as e:
      return { "errors": str(e) }
  return { "errors": form.errors }, 400
    
@film_routes.route("/<int:id>", methods=["PUT"])
def edit_film(id):
  form = FilmForm()

  form["csrf_token"].data = request.cookies["csrf_token"]

  if form.validate_on_submit():
    film = Film.query.get(id)

    film.title = form.data["title"]
    film.year = form.data["year"]
    film.plot = form.data["plot"]
    film.photo_url = form.data["photo_url"]
    film.genre_id = form.data["genre_id"]

    # dealing with db.relationship by appending to new list, and replacing old
    # cast relationship list with new list
    cast = []
    for actor_id in form.data["cast"]:
      actor = Actor.query.get(actor_id)
      cast.append(actor)
    film.cast = cast
    
    try:
      db.session.add(film)
      db.session.commit()
    except Exception as e:
      return { "errors": str(e) }, 500
    return film.to_dict(), 200
  
  return { "errors": form.errors }, 400
