from app.models import db, Film, Actor
from app import app

from datetime import date

with app.app_context():
  
  db.drop_all()
  db.create_all()
  
  actor1 = Actor(
    name = "Nicolas Cage",
    date_of_birth = date(1964, 1, 7),
    photo = "https://www.syfy.com/sites/syfy/files/styles/blog-post-embedded--tablet/public/2020/09/1498576162376-cage12.jpeg"
  )
  
  actor2 = Actor(
    name = "Elizabeth Shue",
    date_of_birth = date(1963, 10, 6),
    photo = "https://m.media-amazon.com/images/M/MV5BOWFkZTIxN2ItODhlOC00MDMwLWEyYTEtZWMxNWQ2MzU3ZjZmXkEyXkFqcGdeQXVyNjk1MjYyNTA@._V1_.jpg"
  )
  
  actor3 = Actor(
    name = "Lakeith Stanfield",
    date_of_birth = date(1991, 8, 12),
    photo = "https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/06/maxresdefault.jpg"
  )
  
  actor4 = Actor(
    name = "Danny Glover",
    date_of_birth = date(1946, 7, 22),
    photo = "https://static.tvtropes.org/pmwiki/pub/images/creatordannyglover_9740.jpg"
  )

  actor5 = Actor(
    name = "Stephen Yuen",
    date_of_birth = date(1983, 12, 21),
    photo = "https://pyxis.nymag.com/v1/imgs/92c/e6b/bc57c5f27ecd49990bcdab824afe9a8afa-05-steven-yeun-feature.2x.h600.w512.jpg"
  )
  
  film1 = Film(
    title = "Leaving Las Vegas",
    year = 1991,
    plot = """
    Ben Sanderson, a Hollywood screenwriter who lost everything because of his alcoholism, arrives in Las Vegas to drink himself to death. There, he meets and forms an uneasy friendship and non-interference pact with prostitute Sera.
    """,
    cast = [actor1, actor2]
    )
  
  film2 = Film(
    title = "Sorry to Bother You",
    year = 2018,
    plot = """
    In an alternate present-day version of Oakland, telemarketer Cassius Green discovers a magical key to professional success, propelling him into a universe of greed.
    """,
    cast = [actor3, actor4]
  )
  
  actors = [actor1, actor2]
  films = [film1, film2]
  
  for actor in actors:
    db.session.add(actor)
  for film in films:
    db.session.add(film)

  db.session.commit()