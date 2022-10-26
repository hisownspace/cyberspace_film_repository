from datetime import date
from app.models.db import db

film_cast = db.Table(
  "film_cast",
  db.Column("film_id", db.ForeignKey("films.id")),
  db.Column("actor_id", db.ForeignKey("actors.id"))
)
db.Table

class Actor(db.Model):
  __tablename__ = "actors"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  date_of_birth = db.Column(db.Date, nullable=True)
  date_of_death = db.Column(db.Date, nullable=True)
  photo = db.Column(db.String(500), nullable=False)

  filmography = db.relationship("Film",
                                secondary=film_cast,
                                back_populates="cast")
  
  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "date_of_birth": date.strftime(self.date_of_birth, "%B %-d, %Y"),
      "date_of_death": self.date_of_death,
      "photo": self.photo
    }
