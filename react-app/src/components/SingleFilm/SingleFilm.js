import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import NotFound from "../NotFound";
import DeleteFilmModal from '../DeleteFilmModal';
import ActorCard from "../ActorCard";

function SingleFilm () {
  const filmId = useParams().id
  const [loaded, setLoaded] = useState(false);
  const [errors, setErrors] = useState(false);
  const [film, setFilm] = useState({});

  // const { id } = useParams();
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/films/${filmId}`);
        const data = await res.json();
      if (res.ok) {
        setFilm(data);
      } else {
        console.log(data.errors);
        setErrors(data.errors);
      }
    })().then(setLoaded(true));
    return () => setLoaded(false);
  }, [filmId]);

  if (errors) {
    return <NotFound />
  } else if (loaded) {
    return (
        <div className="single-film-main">
          <div className="single-film-top">
          {film ?
          <div className="single-film-focus">
            <div className="single-film-heading">
              {film.title}
            </div>
            <div className="single-film-photo-container">
              <img alt={film.title} className="single-film-photo" src={film.image_url} />
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
              <div>
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
              <div className="delete-and-edit-film">
                <a className="edit-actor-link" href={`/films/${film.id}/edit`}>Edit Film</a>
                    &emsp;
                    <div className="delete-actor-link" onClick={() => setShowModal(true)}>Delete Film</div>
              </div>
            </div>

          </div>
          : null}
 
          </div>
          <div className="film-extra-detail">
              <h2>Top Cast:</h2>
              <div className="single-film-cast-cards">
                {film?.cast?.map(actor => {
                  return <ActorCard actor={actor} />
                })}
              </div>
          </div>
          <DeleteFilmModal showModal={showModal} setShowModal={setShowModal} title={film?.title} id={film?.id} />
       </div>
    )
  } else {
    return null;
  }

};

export default SingleFilm;