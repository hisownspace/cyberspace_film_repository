from app import app
from app.models import Actor
from pprint import pprint


with app.app_context():

  actor = Actor.query.get(1)

  pprint(actor)
  pprint(type(actor))
  pprint(actor.to_dict())
  
  # actors = Actor.query.all()
  
  # pprint(actors)
  # pprint(type(actors))
  # pprint({ actor.id: actor.to_dict() for actor in actors })