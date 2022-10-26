from flask import Blueprint

from app.models.actors import Actor

actor_routes = Blueprint("api/actors", __name__)

@actor_routes.route("")
def all_actors():
  """"""
  # return actors
  actors = Actor.query.all()
  return { actor.id: actor.to_dict() for actor in actors }, 200

@actor_routes.route("/<int:id>", methods=["GET", "POST"])
def one_actor(id):
  # actor = ActorForm()
  # if form.validate_on_submit():
  #   pass
  actor = Actor.query.get(id)
  return { actor.id: actor.to_dict() }, 200
  
@actor_routes.route("/count")
def actor_count():
  return { "totalActors": Actor.query.count() }
