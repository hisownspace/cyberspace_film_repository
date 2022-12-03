from flask import Blueprint, request
from datetime import date

from app.models import db, Actor, Film

from app.forms.ActorForm import ActorForm

actor_routes = Blueprint("api/actors", __name__, url_prefix="/api/actors")

@actor_routes.route("", methods=["GET", "POST"])
def all_actors():
  """"""
  form = ActorForm()

  if form.validate_on_submit():

    filmography = form.data["filmography"]
    for idx, id in enumerate(filmography):
      film = Film.query.get(id)
      filmography[idx] = film

    params = {
      "name": form.data["name"],
      "date_of_birth": form.data["date_of_birth"],
      "place_of_birth": form.data["place_of_birth"],
      "photo_url": form.data["photo_url"],
      "bio": form.data["bio"],
      "filmography": filmography
    }
    actor = Actor(**params)

    db.session.add(actor)
    db.session.commit()

    return actor.to_dict(), 201, { "Content-Type": "application/json" }
  
  elif form.errors:
    return { "errors": form.errors }, 409, { "Content-Type": "application/json" }
  else:
    actors = Actor.query.all()
    return { actor.id: actor.to_dict() for actor in actors }, 200, { "Content-Type": "application/json" }

@actor_routes.route("/<int:id>") 
def one_actor(id):
  actor = Actor.query.get(id)
  if actor:
    return { actor.id: actor.to_dict() }, 200, { "Content-Type": "application/json" }
  return { "errors": "Actor not found!" }, 404, { "Content-Type": "application/json" }
  
@actor_routes.route("/count")
def actor_count():
  return { "totalActors": Actor.query.count() }, 200, { "Content-Type": "application/json" }

@actor_routes.route("/<int:id>", methods=["DELETE"])
def delete_actor(id):
  actor = Actor.query.get(id)
  if actor:
    db.session.delete(actor)
    db.session.commit()
    return { "message": f"Successfully deleted {actor.name}" }, 204, { "Content-Type": "application/json" }
  return { "errors": "Actor not found!" }, 404, { "Content-Type": "application/json" }

@actor_routes.route("/<int:id>", methods=["PUT"])
def update_actor(id):
  form = ActorForm();
  form["csrf_token"].data = request.cookies["csrf_token"]
  # print(form.data)
  if form.validate_on_submit():
    films = []
    for film_id in form.data["filmography"]:
      film = Film.query.get(film_id)
      films.append(film)
    actor = Actor.query.get(id)
    actor.name = form.data["name"]
    actor.date_of_birth = form.data["date_of_birth"]
    actor.place_of_birth = form.data["place_of_birth"]
    actor.photo_url = form.data["photo_url"]
    actor.bio = form.data["bio"]
    actor.filmography = films
    db.session.add(actor)
    db.session.commit()
    return actor.to_dict(), 200, { "Content-Type": "application/json" }
  # print(form.errors)
  return { "errors": form.errors }, 409, { "Content-Type": "application/json" }
    