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

    return actor.to_dict()
  
  elif form.errors:
    return { "errors": form.errors }, 409
  else:
    actors = Actor.query.all()
    return { actor.id: actor.to_dict() for actor in actors }, 200

@actor_routes.route("/<int:id>") 
def one_actor(id):
  actor = Actor.query.get(id)
  if actor:
    return { actor.id: actor.to_dict() }, 200
  return { "errors": "Actor not found!" }, 404
  
@actor_routes.route("/count")
def actor_count():
  return { "totalActors": Actor.query.count() }, 200

@actor_routes.route("/<int:id>", methods=["DELETE"])
def delete_actor(id):
  actor = Actor.query.get(id)
  if actor:
    db.session.delete(actor)
    db.session.commit()
    return { "message": f"Successfully deleted {actor.name}" }, 204
  return { "errors": "Actor not found!" }, 404