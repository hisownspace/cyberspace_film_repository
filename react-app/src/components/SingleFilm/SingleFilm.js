import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import NotFound from "../NotFound";

function SingleFilm () {
  const filmId = useParams().id
  const [loaded, setLoaded] = useState(false);
  const [errors, setErrors] = useState(false);
  const [film, setFilm] = useState({});

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/films/${filmId}`);
      if (res.ok) {
        const film = await res.json();
        setFilm(film);
      } else {
        console.log(res.status);
        setErrors(res.status);
      }
    })().then(setLoaded(true));
    return () => setLoaded(false);
  }, [filmId]);

  if (errors) {
    return <NotFound />
  } else if (loaded) {
    return (
        <div className="single-film-main">
          {film ?
          <div className="single-film-focus">
            <div className="single-film-heading">
              {film.title}
            </div>
            <div className="single-film-photo-container">
              <img alt={film.title} className="single-film-photo" src={film.photo_url} />
            </div>
            <div className="single-film-genre">
              <a href={`/genres/${film.genre?.id}`}className="single-film-genre-tab">
                {film.genre?.name}
              </a>
            </div>
            <div className="single-film-plot">
              {film.plot}
            </div>
            <div className="single-film-cast">
              Stars&emsp;{film?.cast?.map((star, idx) => {
                let castList = <a key={`cast-list-${idx}`} href={`/actors/${star.id}`}>{star.name}</a>
                if (idx !== film.cast.length - 1) {
                  return (
                  <div className="cast-list" key={`actor-list-${idx}`}>
                    {castList}&emsp;-&emsp;
                  </div>
                  )
                }
                return castList;
              })}
            </div>
          </div>
          : null}
        </div>
    )
  } else {
    return null;
  }

};

export default SingleFilm;