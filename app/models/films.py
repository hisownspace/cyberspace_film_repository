from app.models.db import db
# from app.models.actors import film_cast

class Film(db.Model):
  """
  A SQLAlchemy.Model child class representing the Actors table in our database\n
  param title: the title of the movie\n
  :param year: the year in which the movie is made\n
  :param plot: a description of the plot of the film - not required\n
  :param cast: a list of the actors in the movie (m2m through film_cast)\n
  """
  
  __tablename__ = "films"
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  plot = db.Column(db.String(2000), nullable=True)

  cast = db.relationship("Actor", secondary="film_cast", back_populates="filmography")
  
  def to_dict(self):
    """
    Returns a dict representing the film:
    { id,
      title,
      year,
      plot,
      cast
    }
    """
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "plot": self.plot,
      "cast": [actor.id for actor in self.cast]
    }
  