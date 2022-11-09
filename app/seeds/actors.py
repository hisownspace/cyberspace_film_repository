from app.models import db, Actor
from datetime import date

def seed_actors():
  actor1 = Actor(
    name = "Nicolas Cage",
    date_of_birth = date(1964, 1, 7),
    place_of_birth = "Long Beach, California, USA",
    photo_url = "https://www.syfy.com/sites/syfy/files/styles/blog-post-embedded--tablet/public/2020/09/1498576162376-cage12.jpeg",
    bio = """Nicolas Cage was born Nicolas Kim Coppola in Long Beach, California, the son of comparative literature professor August Coppola (whose brother is director Francis Ford Coppola) and dancer/choreographer Joy Vogelsang. He is of Italian (father) and Polish and German (mother) descent. Cage changed his name early in his career to make his own reputation, succeeding brilliantly with a host of classic, quirky roles by the late 1980s.

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
    bio = """Elisabeth Shue was born in Wilmington, Delaware, to Anne Brewster (Wells), who worked for the Chemical Banking Corporation, and James William Shue, a lawyer and real estate developer. She is of German and English ancestry, including descent from Mayflower passengers. Shue's parents divorced while she was in the fourth grade. Owing to the occupational demands of her parents, Shue and her siblings found plenty of time to get into trouble in their suburban neighborhood, but Elisabeth soon enrolled in Wellesley College, an all-female institution which kept her out of trouble.

During her studies, she found a way to make a little extra money by acting in television commercials. Elisabeth became a common sight in ads for Burger King, DeBeers diamonds, and Hellman's mayonnaise. In 1984, she landed a role in the The Karate Kid (1984) as the on-screen girlfriend of Ralph Macchio and a role as the teenage daughter of a military family in the short-lived series Call to Glory (1984). At this time, Shue got herself an acting coach and transferred to Harvard, where she began studying political science.

She continued her acting work with Adventures in Babysitting (1987), Cocktail (1988), Soapdish (1991) and The Marrying Man (1991). Unfortunately, time was catching up with the impressive girl-next-door. Her brother Andrew Shue had almost eclipsed her own fame by landing a starring role in the hit TV series Melrose Place (1992). It was at this time that Elisabeth took a chance on a low-budget, high-risk project entitled Leaving Las Vegas (1995), directed by Mike Figgis. Her gutsy portrayal of a prostitute mixed up with a suicidal alcoholic paid off as she was recognized with a Best Actress nomination at the Academy Awards that year. This was the turning point of her career. What followed was a barrage of film roles, including The Saint (1997), Woody Allen's Deconstructing Harry (1997), Palmetto (1998) and Hollow Man (2000).
"""
  )
  
  actor3 = Actor(
    name = "Lakeith Stanfield",
    date_of_birth = date(1991, 8, 12),
    place_of_birth = "San Bernardino, California, USA",
    photo_url = "https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/06/maxresdefault.jpg",
    bio = """LaKeith Lee Stanfield is an actor and rapper from Victorville, California. At the age of fifteen, LaKeith began attending the John Casablancas Modeling & Career Center in Orange County. A few years later, he auditioned for Destin Cretton's then college thesis film Short Term 12 (2008). Later, the newer version of Short Term 12 (2013) marked LaKeith's debut as a professional actor. Subsequently, he landed a role in the Martin Luther King biopic, Selma (2014), and has since starred in Get Out (2017), Knives Out (2019), The Photograph (2020), and the series Atlanta on FX.    
"""
  )
  
  dan_glove = Actor(
    name = "Danny Glover",
    date_of_birth = date(1946, 7, 22),
    place_of_birth = "San Francisco, California, USA",
    photo_url = "https://static.tvtropes.org/pmwiki/pub/images/creatordannyglover_9740.jpg",
    bio = """Actor, producer and humanitarian Danny Glover has been a commanding presence on screen, stage and television for more than 35 years.

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
    bio = """Steven Yeun was born in Seoul, South Korea, to June and Je Yeun. His family first immigrated to Canada and stayed there for one year, and then moved to the U.S. He has a brother named Brian. He began acting while at Kalamazoo College in Kalamazoo, MI, where he studied Psychology as a major (BS in Psychology, 2005). When he realized his love for acting he went to study theatre in college instead of med school. He was a member of Stir Friday Night, a sketch-comedy group made up of Asian-American performers, and was also a member of the Second City comedy troupe in Chicago. He earned roles on The Big Bang Theory (2007) (as Sebastian), in Jerry (2009) (as Chaz) and in different commercials for Best Buy, Apple, and Milky Way. He lives in L.A.

Steven enjoys playing guitar. His parents own beauty supply stores in Detroit, MI.    
"""
  )

  jim_fails = Actor(
  name = "Jimmie Fails",
  date_of_birth = date(1994, 11, 10),
  place_of_birth = "San Francisco, California, USA",
  photo_url = "https://m.media-amazon.com/images/M/MV5BZTdkN2QxNTItODAzMi00ZDEzLTgxOGUtNDAzMjBiZjZhNmEyXkEyXkFqcGdeQXVyNDYwMDE4NTA@._V1_.jpg",
  bio = """Jimmie Fails is known for The Last Black Man in San Francisco (2019), Pieces of a Woman (2020) and Borderline."""
  )
  
  jon_majors = Actor(
    name = "Jonathan Majors",
    date_of_birth = date(1989, 9, 7),
    place_of_birth = "Lompoc, California, USA",
    photo_url = "https://m.media-amazon.com/images/M/MV5BYTQ0ZDkzZmYtYzAzZC00YTUwLWJhZmEtZGRjZTQyYWUwYWI0XkEyXkFqcGdeQXVyMjU2Nzg3NzM@._V1_.jpg",
    bio = '''Majors is a graduate from the Yale School of Drama and is a recipient of the National Society of Arts and Letters (NSAL), National Drama Competition. He made his screen debut starring in the ABC miniseries "When We Rise" and has since landed strong roles, cementing him as a Hollywood actor to watch. For his role as Montgomery Allen in The Last Black Man in San Francisco, Majors was nominated for a Gotham Award in the category of "Breakthrough Actor" and an Independent Spirit Award for "Best Supporting Male."'''
  )
  
  rob_morgan = Actor(
    name = "Rob Morgan",
    date_of_birth = date(1973, 2, 24),
    place_of_birth = "New Bern, North Carolina, USA",
    photo_url = "https://m.media-amazon.com/images/M/MV5BYTA4YTIwOTItZTg1Yy00NDk3LTkwMTItYTFhMjhkYzVjYTQxXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
    bio =  """Rob Morgan was born on February 24, 1973 in New Bern, Craven County, North Carolina, USA. He is an actor, known for Mudbound (2017), Don't Look Up (2021) and Bull (2019)."""
  )
  
  zaz_beetz = Actor(
    name = "Zazie Beetz",
    date_of_birth = date(1991, 6, 1),
    place_of_birth = "Mitte, Berlin, Germany",
    photo_url = "https://m.media-amazon.com/images/M/MV5BOGQxMjRiY2QtZDk1My00NmU1LTgxZDctOGI0YTA4OGYzMmY5XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_FMjpg_UX650_.jpg",
    bio = """Zazie Beetz (born c. 1991) is a German-American actress known for the role of Vanessa on Atlanta (2016), as well as for starring in Deadpool 2 (2018), Joker (2019), and Nine Days (2020).

Born in Berlin to a German father and an African-American mother, Beetz was raised in New York speaking both German and English at home. Performing in community theaters and local stages since childhood, Zazie found her joy in grade school and grew up acting. She attended LaGuardia Arts High school, where she continued to engage her love for performing arts, but decided to not pursue a conservatory program afterward. Instead, she went to Skidmore College, where she received a bachelor's degree in French. Beetz currently resides in her hometown, New York."""
  )

  ed_elb = Actor(
    name ="Idris Elba",
    date_of_birth = date(1972, 9, 6),
    place_of_birth = "Hackney, London, England, UK",
    photo_url = "https://m.media-amazon.com/images/M/MV5BNzEzMTI2NjEyNF5BMl5BanBnXkFtZTcwNTA0OTE4OA@@._V1_.jpg",
    bio = """An only child, Idrissa Akuna Elba was born and raised in London, England. His father, Winston, is from Sierra Leone and worked at Ford Dagenham; his mother, Eve, is from Ghana and had a clerical duty. Idris attended school in Canning Town, where he first became involved in acting, before he dropped out. He gained a place in the National Youth Music Theatre - thanks to a £1,500 Prince's Trust grant. To support himself between acting roles, he worked in jobs such as tyre-fitting, cold call advertising sales, and working night shifts at Ford Dagenham. He worked in nightclubs under the nickname DJ Big Driis at age 19, but began auditioning for television roles in his early-twenties.

His first acting roles were on the soap opera Family Affairs (1997), the television serial Ultraviolet (1998), and the medical drama Dangerfield (1995). His best known roles are as drug baron Russell "Stringer" Bell on the HBO series The Wire (2002), as DCI John Luther on the BBC One series Luther (2010), and as Heimdall in the Marvel Cinematic Universe. He later starred in the films Daddy's Little Girls (2007), Prom Night (2008), RocknRolla (2008), The Unborn (2009) and Obsessed (2009). He also appeared in the films American Gangster (2007), Takers (2010), Thor (2011), Prometheus (2012), Pacific Rim (2013), Thor: The Dark World (2013), Beasts of No Nation (2015) and Star Trek Beyond (2016). He voiced Chief Bogo in Zootopia (2016), Shere Khan in The Jungle Book (2016), and Fluke in Finding Dory (2016).

Idris Elba was appointed Officer of the Order of the British Empire (OBE) by Queen Elizabeth II in the 2016 New Years Honours for his services to drama."""
  )
  reg_king = Actor(
    name = "Regina King",
    date_of_birth = date(1971, 1, 15),
    place_of_birth = "Los Angeles, California, USA",
    photo_url = "https://m.media-amazon.com/images/M/MV5BZGM1M2I1ZWQtNWVmMC00YTE4LWFiNDEtNWVlN2FmNmU5MjZjXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg",
    bio = """Regina King was born in Los Angeles, California, to Gloria, a special education teacher, and Thomas King, an electrician. She began her career in the television show 227 (1985), followed by a role in Boyz n the Hood (1991). She began to be recognized by a mainstream audience after her role as Cuba Gooding Jr.'s character's wife in Jerry Maguire (1996). She co-starred in Enemy of the State (1998) as Will Smith's character's wife."""
  )
  
  til_swin = Actor(
    name = "Tilda Swinton",
    date_of_birth = date(1960, 11, 5),
    place_of_birth = "London, England, UK",
    photo_url = "https://m.media-amazon.com/images/M/MV5BMTM4NzMzMTkwNV5BMl5BanBnXkFtZTcwMzU4MDg1Mw@@._V1_FMjpg_UX319_.jpg",
    bio = """The iconoclastic gifts of the highly striking and ferociously talented actress Tilda Swinton have been appreciated by art house crowds and international audiences alike. After her stunning Oscar-winning turn as a high-powered corporate attorney in the George Clooney starring and critically-lauded legal thriller Michael Clayton (2007), however, her androgynous looks and often bizarre appeal have been embraced by more mainstream crowds as well.

She was born Katherine Mathilda Swinton into a patrician Scottish military family on November 5, 1960, in London, England. Her mother, Judith Balfour, Lady Swinton (née Killen), was Australian, and her father, Major-General Sir John Swinton, an army officer, was English-born. Her ancestry is Scottish, Northern Irish, and English, including a long tapestry of prominent Scottish ancestors. Educated at an English and a Scottish boarding school, Tilda subsequently studied Social and Political Science at Cambridge University and graduated in 1983 with a degree in English Literature.

During her tenure as a student, she performed countless stage productions and proceeded to work for a season with the Royal Shakespeare Company where she appeared in such productions as "Measure for Measure." The rebel insider her, however, was strong and she left the company after a year as her approach and interests began to shift dramatically. With a pungent taste for the unique and seldom tried, Tilda found some gender-bending stage roles come her way. She portrayed Mozart in Pushkin's "Mozart and Salieri", and as a working class woman impersonating her dead husband during World War II, in Manfred Karge's "Man to Man," a role she later committed to film (Screenplay: Man to Man (1992)).

In 1985, the tall, slender performer with alabaster skin and carrot-topped hair began a professional association with gay experimental director Derek Jarman. She continued to live and work with the groundbreaking writer/director/cinematographer for the next nine years, involving herself in seven of his often notorious films. This quirky, highly fascinating alliance would produce such stark and radical turns as the Berlin International Film Festival winners Caravaggio (1986), The Last of England (1987), The Garden (1990) and Edward II (1991) (playing Isabella, in which she won "Best Actress" at the Venice Film Festival) and Wittgenstein (1993), as well as the films Soursweet (1988) (a movie with no spoken dialogue) and the Stockholm Film Festival Award winner Blue (1993).

Jarman succumbed to complications from AIDS in 1994. His untimely demise left a devastating void in Tilda's life for quite some time. Her most notable performance of her Jarman period, however, came from a non-Jarman film. For the vivid title role in Orlando (1992), her nobleman character lives for 400 years while changing sex from man to woman. The film, which Swinton spent years helping writer/director Sally Potter develop and finance, continues to this day to have a worldwide devoted fan following.

Over the years, Tilda has preferred art to celebrity, opening herself to experimental projects with new and untried directors and mediums, delving into the worlds of installation art and cutting-edge fashion. Consistently off-centered roles in Female Perversions (1996), Love Is the Devil: Study for a Portrait of Francis Bacon (1998), Teknolust (2002), Young Adam (2003), Broken Flowers (2005) and Béla Tarr's The Man from London (2007) have added to her mystique. Back in 1995, she delved into a performance art piece in the Serpentine Gallery, London, where she was put on display to the public for a week, asleep (or apparently so), in a glass case.

Following the birth of her twins in 1997, Tilda would leave lean for a time towards Hollywood mainstream filming. The thriller The Deep End (2001), earned her a number of critic's awards and her first Golden Globe nomination. Other visible U.S. pictures included The Beach (2000) with Leonardo DiCaprio, fantasy epic Constantine (2005) with Keanu Reeves, her Oscar-decorated performance in Michael Clayton (2007) and, of course, her iconic White Witch in The Chronicles of Narnia: The Lion, the Witch and the Wardrobe (2005).

Into the millennium, Tilda continued to amaze starring in the crime drama Julia (2008) and in David Fincher's The Curious Case of Benjamin Button (2008). She learned Italian and Russian for Luca Guadagnino's I Am Love (2009), starred in the psychological thriller We Need to Talk About Kevin (2011), Wes Anderson's Moonrise Kingdom (2012) and Bong Joon Ho's Snowpiercer (2013), and earned fine notice in Terry Gilliam's The Zero Theorem (2013). She also starred in the dark romantic fantasy drama Only Lovers Left Alive (2013) directed by Jim Jarmusch, had a small role in Wes Anderson's The Grand Budapest Hotel (2014), starred in Judd Apatow's comedy Trainwreck (2015), and played a rock star in Luca Guadagnino's A Bigger Splash (2015).

Showing no signs of slowing up, Tilda continues to make creative, visual impressions in such films as the Coen Brothers' Hail, Caesar! (2016) where she reunited with Clooney and had a dual role playing twin journalists, and as the wise Asian teacher of Dr. Strange (Benedict Cumberbatch) in the Marvel Comics action film Doctor Strange (2016), while repeating the part of The Ancient One in Avengers: Endgame (2019). She gave another eccentric, unhinged performance in the action adventure message movie Okja (2017), played Betsy Trotwood in a contemporary telling of The Personal History of David Copperfield (2019) and teamed up again with writer/director Jim Jarmusch in the thoroughly offbeat fantasy horror comedy The Dead Don't Die (2019)."""
  )
  
  seo_ahn = Actor(
    name = "Seo-hyun Ahn",
    date_of_birth = date(2004, 1, 12),
    place_of_birth = "Suwon, South Korea",
    photo_url = "https://m.media-amazon.com/images/M/MV5BMjAzNDg3MzE1OV5BMl5BanBnXkFtZTgwMTQwNDU5MDI@._V1_.jpg",
    bio = """Seo-hyun Ahn was born on January 12, 2004 in Suwon, South Korea. She is an actress, known for Okja (2017), The Housemaid (2010) and The Yellow Sea (2010)."""
  )
  

  actors = {
    "nic_cage": actor1,
    "liz_shu": actor2,
    "lak_stan": actor3,
    "dan_glove": dan_glove,
    "steve_yeun": actor5,
    "jim_fails": jim_fails,
    "jon_majors": jon_majors,
    "rob_morgan": rob_morgan,
    "zaz_beetz": zaz_beetz,
    "ed_elb": ed_elb,
    "reg_king": reg_king,
    "til_swin": til_swin,
    "seo_ahn": seo_ahn
  }
  
  [db.session.add(actor) for actor in actors.values()]
  db.session.commit()
  print("ACTORS SEEDED TO DATABASE!")
  return actors

def undo_actors():
  db.session.execute('DELETE FROM actors;')
  db.session.commit()
  print("ACTORS REMOVED FROM DATABASE!")