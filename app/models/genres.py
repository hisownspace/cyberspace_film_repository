from app.models.db import db

class Genre(db.Model):
  """
  A SQLAlchemy.Model child class representing the genres table in our database
  
  :param name: the name of the genre
  
  :param filmography: a list of the films that are classified under this genre (m2m through film_genre)
  """
  __tablename__ = "genres"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True)
  
  films = db.relationship("Film", back_populates="genre")

  def to_dict(self, from_film=False):
    return {
      "id": self.id,
      "name": self.name,
      "films": [film.id for film in self.films] if from_film else { film.to_dict(from_genre=True) for film in self.films }
    }