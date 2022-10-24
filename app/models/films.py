from app.models.db import db
from app.models.actors import film_cast

class Film(db.Model):
  __tablename__ = "films"
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  plot = db.Column(db.String(2000), nullable=True)
  