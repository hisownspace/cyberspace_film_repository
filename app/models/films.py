from app.models.db import db
# from app.models.actors import film_cast


class Film(db.Model):
  """
  A SQLAlchemy.Model child class representing the Actors table in our database\n
  @param title: the title of the movie\n
  @param year: the year in which the movie is made\n
  @param plot: a description of the plot of the film - not required\n
  @param photo_url: a link to a photo of the movie poster\n
  @param cast: a list of the actors in the movie (m2m through film_cast)\n
  """
  
  __tablename__ = "films"
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  plot = db.Column(db.String(2000), nullable=True)
  photo_url = db.Column(db.String(1000), nullable=False)
  genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)  
  
  
  genre = db.relationship("Genre", back_populates="films")

  cast = db.relationship("Actor", secondary="film_cast", back_populates="filmography")
  
  def to_dict(self, from_actor=False, from_genre=False):
    """
    Returns a dict representing the film:
    { id,
      title,
      year,
      plot,
      photo_url,
      cast
    }
    """
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "plot": self.plot,
      "photo_url": self.photo_url,
      "cast": [actor.id for actor in self.cast] if from_actor else [actor.to_dict(True) for actor in self.cast],
      "genre": self.genre.id if from_genre else self.genre.to_dict(from_film=True)
    }
  