from flask.cli import AppGroup
from .actors import seed_actors, undo_actors
from .films import seed_films, undo_films, undo_film_cast
from .genres import seed_genres, undo_genres

seed_commands = AppGroup('seed')

@seed_commands.command("all")
def seed():
  actors = seed_actors()
  genres = seed_genres()
  seed_films(actors, genres)
  
@seed_commands.command("undo")
def undo():
  undo_actors()
  undo_genres()
  undo_films()
  undo_film_cast()