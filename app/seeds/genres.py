from app.models import db, Genre

def seed_genres():
  genres = {
  "fantasy": Genre(name = "Fantasy"),
  "horror": Genre(name = "Horror"),
  "action": Genre(name = "Action"),
  "sci_fi": Genre(name = "Sci-fi"),
  "comedy": Genre(name = "Comedy"),
  "drama": Genre(name = "Drama"),
  "western": Genre(name="Western")
  }
  
  [db.session.add(genre) for genre in genres.values()]
  db.session.commit()
  print("GENRES SEEDED TO DATABASE!")

  return genres

def undo_genres():
  db.session.execute('DELETE FROM genres;')
  db.session.commit()
  print("GENRES REMOVED FROM DATABASE!")

