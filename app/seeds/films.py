from app.models import db, Film, Actor, Genre

def seed_films(actors, genres):
  
  actor1, actor2, actor3, dan_glove, steve_yeun, jim_fails, jon_majors, rob_morgan, zaz_beetz, ed_elb, reg_king, til_swin, seo_ahn = actors.values()
  fantasy, horror, action, sci_fi, comedy, drama, western = genres.values()
  
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
    cast = [actor3, dan_glove, steve_yeun],
    photo_url = 'https://m.media-amazon.com/images/M/MV5BNjgwMmI4YzUtZGI2Mi00M2MwLWIyMmMtZWYzMWZmNzAyNmYwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
    genre = sci_fi
  )

  film3 = Film(
    title = "The Last Black Man in San Francisco",
    year = 2019,
    plot ="""A young man searches for home in the changing city that seems to have left him behind.""",
    cast = [jim_fails, jon_majors, rob_morgan, dan_glove],
    photo_url = "https://m.media-amazon.com/images/M/MV5BNTQ5OTUwYjQtYmM5Ni00YTY5LWFiOWEtYTg1MTg2Y2NmY2JhXkEyXkFqcGdeQXVyMTAzNjk5MDI4._V1_.jpg",
    genre = drama
  )
  
  film4 = Film(
    title = "The Harder They Fall",
    year = 2021,
    plot = """When an outlaw discovers his enemy is being released from prison, he reunites his gang to seek revenge.""",
    cast = [jon_majors, zaz_beetz, ed_elb, reg_king],
    photo_url = "https://m.media-amazon.com/images/M/MV5BZTQwYThhZTYtZTQ3MC00NDQ0LWFkZGMtMzdiMTU3OGJiYTY0XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
    genre = western
  )
  
  okja = Film(
    title = "Okja",
    year = 2017,
    plot = """A young girl risks everything to prevent a powerful, multinational company from kidnapping her best friend - a fascinating beast named Okja.""",
    cast = [steve_yeun, til_swin, seo_ahn],
    photo_url = "https://m.media-amazon.com/images/M/MV5BMjQxMTcxNDgxN15BMl5BanBnXkFtZTgwOTczNTIzMjI@._V1_FMjpg_UX509_.jpg",
    genre = drama 
  )
  
  snowden = Film(
    
  )
  
  films = {
    "leaving_las_vegas": film1,
    "sorry_to_bother_you": film2,
    "the_last_black_man_in_san_francisco": film3,
    "the_harder_they_fall": film4,
    "okja": okja,    
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