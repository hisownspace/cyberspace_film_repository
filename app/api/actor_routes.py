from flask import Blueprint

from app.models.actors import all_actors as actors

actor_routes = Blueprint("api/actors", __name__)


@actor_routes.route("/")
def all_actors():
  # return actors
  return { "actors": actors }

@actor_routes.route("/<int:id>")
def one_actor(id):
  print("in the route")
  actor_in_list = next((x for x in actors if x["id"] == id), None)
  if not actor_in_list:
    return { "errors": "Actor not found!" }
  return { "actor": actor_in_list }
  
  