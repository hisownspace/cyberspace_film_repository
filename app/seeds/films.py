from app.models import db, Film, Actor, Genre

def seed_films(actors, genres):
  
  actor1, actor2, actor3, actor4, actor5 = actors.values()
  fantasy, horror, action, sci_fi, comedy, drama = genres.values()
  
  film1 = Film(
    title = "Leaving Las Vegas",
    year = 1991,
    plot = """Ben Sanderson, a Hollywood screenwriter who lost everything because of his alcoholism, arrives in Las Vegas to drink himself to death. There, he meets and forms an uneasy friendship and non-interference pact with prostitute Sera.
    """,
    cast = [actor1, actor2],
    photo_url = 'https://m.media-amazon.com/images/M/MV5BNDg3MDM5NTI0MF5BMl5BanBnXkFtZTcwNDY0NDk0NA@@._V1_.jpg',
    genre = drama
  )
  
  film2 = Film(
    title = "Sorry to Bother You",
    year = 2018,
    plot = """In an alternate present-day version of Oakland, telemarketer Cassius Green discovers a magical key to professional success, propelling him into a universe of greed.
    """,
    cast = [actor3, actor4, actor5],
    photo_url = 'https://m.media-amazon.com/images/M/MV5BNjgwMmI4YzUtZGI2Mi00M2MwLWIyMmMtZWYzMWZmNzAyNmYwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
    genre = sci_fi
  )
  
  films = {
    "leaving_las_vegas": film1,
    "sorry_to_bother_you": film2
    }
  
  [db.session.add(film) for film in films.values()]
  db.session.commit()
  
  print("FILMS SEEDED TO DATABASE!")

def undo_films():
  db.session.execute('DELETE FROM films;')
  db.session.commit()
  print("FILMS REMOVED FROM DATABASE!")

def undo_film_cast():
  db.session.execute("DELETE FROM film_cast;")
  db.session.commit()
  print("FILM_CAST REMOVED FROM DATABASE")