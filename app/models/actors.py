from sqlalchemy import ForeignKey
from app.models.db import db

film_cast = db.Table(
  "film_cast",
  db.Column("film_id", ForeignKey="actors.id"),
  db.Column("actor_id", ForeignKey="films.id")
)
db.Table


class Actor(db.Model):
  __tablename__ = "actors"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  date_of_birth = db.Column(db.Date, nullable=True)
  date_of_death = db.Column(db.Date, nullable=True)

  filmography = db.relationship("Film",
                                secondary=film_cast,
                                back_populates="cast")

all_actors = [
  {"id": 1, "name": "Nicholas Cage" },
  { "id": 2, "name": "Natalie Portman" },
  { "id": 3, "name": "Keanu Reeves" },
  { "id": 4, "name": "Viola Davis" },
  { "id": 5, "name": "Denzel Washington" },
  { "id": 6, "name": "Regina King" },
  { "id": 7, "name": "Daniel Day Lewis" },
  { "id": 8, "name": "Val Kilmer" },
  { "id": 9, "name": "Lakeith Stanfield" },
  { "id": 10, "name": "Danny Glover" }
]