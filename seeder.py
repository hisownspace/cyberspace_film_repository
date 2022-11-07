from app.models import db, Film, Actor, Genre
from app import app

from datetime import date

with app.app_context():
  
  db.drop_all()
  db.create_all()
  
  
  fantasy = Genre(name = "Fantasy") 
  horror = Genre(name = "Horror")
  action = Genre(name = "Action")
  sci_fi = Genre(name = "Sci-fi")
  comedy = Genre(name = "Comedy")
  drama = Genre(name = "Drama")
  
  actor1 = Actor(
    name = "Nicolas Cage",
    date_of_birth = date(1964, 1, 7),
    place_of_birth = "Long Beach, California, USA",
    photo_url = "https://www.syfy.com/sites/syfy/files/styles/blog-post-embedded--tablet/public/2020/09/1498576162376-cage12.jpeg",
    bio = """
Nicolas Cage was born Nicolas Kim Coppola in Long Beach, California, the son of comparative literature professor August Coppola (whose brother is director Francis Ford Coppola) and dancer/choreographer Joy Vogelsang. He is of Italian (father) and Polish and German (mother) descent. Cage changed his name early in his career to make his own reputation, succeeding brilliantly with a host of classic, quirky roles by the late 1980s.

Initially studying theatre at Beverly Hills High School (though he dropped out at seventeen), he secured a bit part in Fast Times at Ridgemont High (1982) -- most of which was cut, dashing his hopes and leading to a job selling popcorn at the Fairfax Theater, thinking that would be the only route to a movie career. But a job reading lines with actors auditioning for uncle Francis' Rumble Fish (1983) landed him a role in that film, followed by the punk-rocker in Valley Girl (1983), which was released first and truly launched his career.

His one-time passion for method acting reached a personal limit when he smashed a street-vendor's remote-control car to achieve the sense of rage needed for his gangster character in The Cotton Club (1984).

In his early 20s, he dated Jenny Wright for two years and later linked to Uma Thurman. After a relationship of several years with Christina Fulton, a model, they split amicably and share custody of a son, Weston Cage (b. 1990). He also has a son with his ex-wife, Alice Kim Cage.
"""
  )
  
  actor2 = Actor(
    name = "Elizabeth Shue",
    date_of_birth = date(1963, 10, 6),
    place_of_birth = "Wilmington, Delaware, USA",
    photo_url = "https://m.media-amazon.com/images/M/MV5BOWFkZTIxN2ItODhlOC00MDMwLWEyYTEtZWMxNWQ2MzU3ZjZmXkEyXkFqcGdeQXVyNjk1MjYyNTA@._V1_.jpg",
    bio = """
Elisabeth Shue was born in Wilmington, Delaware, to Anne Brewster (Wells), who worked for the Chemical Banking Corporation, and James William Shue, a lawyer and real estate developer. She is of German and English ancestry, including descent from Mayflower passengers. Shue's parents divorced while she was in the fourth grade. Owing to the occupational demands of her parents, Shue and her siblings found plenty of time to get into trouble in their suburban neighborhood, but Elisabeth soon enrolled in Wellesley College, an all-female institution which kept her out of trouble.

During her studies, she found a way to make a little extra money by acting in television commercials. Elisabeth became a common sight in ads for Burger King, DeBeers diamonds, and Hellman's mayonnaise. In 1984, she landed a role in the The Karate Kid (1984) as the on-screen girlfriend of Ralph Macchio and a role as the teenage daughter of a military family in the short-lived series Call to Glory (1984). At this time, Shue got herself an acting coach and transferred to Harvard, where she began studying political science.

She continued her acting work with Adventures in Babysitting (1987), Cocktail (1988), Soapdish (1991) and The Marrying Man (1991). Unfortunately, time was catching up with the impressive girl-next-door. Her brother Andrew Shue had almost eclipsed her own fame by landing a starring role in the hit TV series Melrose Place (1992). It was at this time that Elisabeth took a chance on a low-budget, high-risk project entitled Leaving Las Vegas (1995), directed by Mike Figgis. Her gutsy portrayal of a prostitute mixed up with a suicidal alcoholic paid off as she was recognized with a Best Actress nomination at the Academy Awards that year. This was the turning point of her career. What followed was a barrage of film roles, including The Saint (1997), Woody Allen's Deconstructing Harry (1997), Palmetto (1998) and Hollow Man (2000).
"""
  )
  
  actor3 = Actor(
    name = "Lakeith Stanfield",
    date_of_birth = date(1991, 8, 12),
    place_of_birth = "San Bernardino, California, USA",
    photo_url = "https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/06/maxresdefault.jpg",
    bio = """
LaKeith Lee Stanfield is an actor and rapper from Victorville, California. At the age of fifteen, LaKeith began attending the John Casablancas Modeling & Career Center in Orange County. A few years later, he auditioned for Destin Cretton's then college thesis film Short Term 12 (2008). Later, the newer version of Short Term 12 (2013) marked LaKeith's debut as a professional actor. Subsequently, he landed a role in the Martin Luther King biopic, Selma (2014), and has since starred in Get Out (2017), Knives Out (2019), The Photograph (2020), and the series Atlanta on FX.    
"""
  )
  
  actor4 = Actor(
    name = "Danny Glover",
    date_of_birth = date(1946, 7, 22),
    place_of_birth = "San Francisco, California, USA",
    photo_url = "https://static.tvtropes.org/pmwiki/pub/images/creatordannyglover_9740.jpg",
    bio = """
Actor, producer and humanitarian Danny Glover has been a commanding presence on screen, stage and television for more than 35 years.

Glover was born in San Francisco, California, to Carrie (Hunley) and James Glover, postal workers who were also active in civil rights. Glover trained at the Black Actors' Workshop of the American Conservatory Theater. It was his Broadway debut in Fugard's Master Harold...and the Boys, which brought him to national recognition and led director Robert Benton to cast Glover in his first leading role in 1984's Oscar®-nominated Best Picture Places in the Heart.

The following year, Glover starred in two more Best Picture nominees: Peter Weir's Witness and Steven Spielberg's The Color Purple. In 1987, Glover partnered with Mel Gibson in the first Lethal Weapon film and went on to star in three hugely successful Lethal Weapon sequels. Glover has also invested his talents in more personal projects, including the award-winning To Sleep With Anger, which he executive produced and for which he won an Independent Spirit Award for Best Actor; Bopha!; Manderlay; Missing in America; and the film version of Athol Fugard's play Boesman and Lena. On the small screen, Glover won an Image Award and a Cable ACE Award and earned an Emmy nomination for his performance in the title role of the HBO movie Mandela. He has also received Emmy nominations for his work in the acclaimed miniseries Lonesome Dove and the telefilm Freedom Song. As a director, he earned a Daytime Emmy nomination for Showtime's Just a Dream.

Glover's film credits range from the blockbuster Lethal Weapon franchise to smaller independent features, some of which Glover also produced. He co-starred in the critically acclaimed feature Dreamgirls directed by Bill Condon and in Po' Boy's Game for director Clement Virgo. He appeared in the hit feature Shooter for director Antoine Fuqua, Honeydripper for director John Sayles, and Be Kind, Rewind for director Michel Gondry.

Glover has also gained respect for his wide-reaching community activism and philanthropic efforts, with a particular emphasis on advocacy for economic justice, and access to health care and education programs in the United States and Africa. For these efforts, Glover received a 2006 DGA Honor. Internationally, Glover has served as a Goodwill Ambassador for the United Nations Development Program from 1998-2004, focusing on issues of poverty, disease, and economic development in Africa, Latin America, and the Caribbean, and serves as UNICEF Ambassador.

In 2005, Glover co-founded Louverture Films dedicated to the development and production of films of historical relevance, social purpose, commercial value and artistic integrity. The New York based company has a slate of progressive features and documentaries including Trouble the Water, which won the Grand Jury Prize at the 2008 Sundance Film Festival, Africa Unite, award winning feature Bamako, and most recent projects Uncle Boonmee Who Can Recall His Past Lives, and The Disappearance of McKinley Nolan.
"""
  )

  actor5 = Actor(
    name = "Steven Yeun",
    place_of_birth = "Seoul, South Korea",
    date_of_birth = date(1983, 12, 21),
    photo_url = "https://pyxis.nymag.com/v1/imgs/92c/e6b/bc57c5f27ecd49990bcdab824afe9a8afa-05-steven-yeun-feature.2x.h600.w512.jpg",
    bio = """
Steven Yeun was born in Seoul, South Korea, to June and Je Yeun. His family first immigrated to Canada and stayed there for one year, and then moved to the U.S. He has a brother named Brian. He began acting while at Kalamazoo College in Kalamazoo, MI, where he studied Psychology as a major (BS in Psychology, 2005). When he realized his love for acting he went to study theatre in college instead of med school. He was a member of Stir Friday Night, a sketch-comedy group made up of Asian-American performers, and was also a member of the Second City comedy troupe in Chicago. He earned roles on The Big Bang Theory (2007) (as Sebastian), in Jerry (2009) (as Chaz) and in different commercials for Best Buy, Apple, and Milky Way. He lives in L.A.

Steven enjoys playing guitar. His parents own beauty supply stores in Detroit, MI.    
"""
  )
  
  film1 = Film(
    title = "Leaving Las Vegas",
    year = 1991,
    plot = """
Ben Sanderson, a Hollywood screenwriter who lost everything because of his alcoholism, arrives in Las Vegas to drink himself to death. There, he meets and forms an uneasy friendship and non-interference pact with prostitute Sera.
    """,
    cast = [actor1, actor2],
    photo_url = 'https://m.media-amazon.com/images/M/MV5BNDg3MDM5NTI0MF5BMl5BanBnXkFtZTcwNDY0NDk0NA@@._V1_.jpg',
    genre = drama
  )
  
  film2 = Film(
    title = "Sorry to Bother You",
    year = 2018,
    plot = """
In an alternate present-day version of Oakland, telemarketer Cassius Green discovers a magical key to professional success, propelling him into a universe of greed.
    """,
    cast = [actor3, actor4, actor5],
    photo_url = 'https://m.media-amazon.com/images/M/MV5BNjgwMmI4YzUtZGI2Mi00M2MwLWIyMmMtZWYzMWZmNzAyNmYwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
    genre = sci_fi
  )
  
  actors = [actor1, actor2, actor3, actor4, actor5]
  films = [film1, film2]
  
  for actor in actors:
    db.session.add(actor)
  for film in films:
    db.session.add(film)

  db.session.commit()