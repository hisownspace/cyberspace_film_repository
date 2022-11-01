from flask import Blueprint
from datetime import date

from app.models import db
from app.models.actors import Actor

from app.forms.ActorForm import ActorForm

actor_routes = Blueprint("api/actors", __name__)

@actor_routes.route("", methods=["GET", "POST"])
def all_actors():
  """"""
  form = ActorForm()
  print(form.data)
  if form.validate_on_submit():
    params = {
      "name": form.data["name"],
      "date_of_birth": form.data["date_of_birth"],
      "place_of_birth": form.data["place_of_birth"],
      "photo": form.data["photo"]
    }
    actor = Actor(**params)

    db.session.add(actor)
    db.session.commit()

    return actor.to_dict()
  # return actors
  print(form.errors)
  if form.errors:
    return { "errors": form.errors }, 409
  actors = Actor.query.all()
  return { actor.id: actor.to_dict() for actor in actors }, 200

@actor_routes.route("/<int:id>") 
def one_actor(id):
  actor = Actor.query.get(id)
  return { actor.id: actor.to_dict() }, 200
  
@actor_routes.route("/count")
def actor_count():
  return { "totalActors": Actor.query.count() }, 200
