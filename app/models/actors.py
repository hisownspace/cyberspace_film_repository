from datetime import date
from app.models.db import db

film_cast = db.Table(
  "film_cast",
  db.Column("film_id", db.Integer, db.ForeignKey("films.id"), primary_key=True),
  db.Column("actor_id", db.Integer, db.ForeignKey("actors.id"), primary_key=True)
)
db.Table

class Actor(db.Model):
  """
  A SQLAlchemy.Model child class representing the Actors table in our database\n
  @param name: the full name of actor\n
  @param date_of_birth: the birthdate of the actor\n
  @param place_of_birth: the date of death of the actor (if applicable)\n
  @param photo_url: a link to a photo of the actor\n 
  @param bio: a short description of the life of the actor\n
  @param filmography: a list of the films the actor has had a role in (m2m through film_cast)\n
  """
  __tablename__ = "actors"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  date_of_birth = db.Column(db.Date, nullable=True)
  place_of_birth = db.Column(db.String(255), nullable=True)
  photo_url = db.Column(db.String(500), nullable=False)
  bio = db.Column(db.String(5000), nullable=True)

  filmography = db.relationship("Film",
                                secondary=film_cast,
                                back_populates="cast")
  
  def to_dict(self, from_film=False):
    """
    Returns a dict representing the Actor
    {
      id,
      name,
      date_of_birth,
      place_of_birth,
      photo
    }
    """
    return {
      "id": self.id,
      "name": self.name,
      "date_of_birth": date.strftime(self.date_of_birth, "%B %-d, %Y"),
      "place_of_birth": self.place_of_birth,
      "photo_url": self.photo_url,
      "bio": self.bio,
      "filmography":  [film.id for film in self.filmography] if from_film else [film.to_dict(True) for film in self.filmography]
    }
