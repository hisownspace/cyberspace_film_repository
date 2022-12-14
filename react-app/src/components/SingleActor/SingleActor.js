import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

import NotFound from '../NotFound';
import DeleteActorModal from '../DeleteActorModal';

const SingleActor = () => {
  const [loaded, setLoaded] = useState(false);
  const [actor, setActor] = useState();
  const [errors, setErrors] = useState(false)

  const { id } = useParams();
  const [showModal, setShowModal] = useState(false);


  
  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/actors/${id}`);
      if (res.ok) {
        const actor = await res.json();
        document.title = `${actor.name} Page`;
        setActor(actor);
      } else {
        setErrors(res.status);
      };
    })().then(setLoaded(true));
    return () => setLoaded(false);
  }, [id]);

  if (errors) {
    return <NotFound />;
  } else if (loaded) {
    return (
      <div className='single-actor-main'>
        {actor ? 
            <div className='single-actor-focus'>
              <div className="single-actor-photo-container">
                <img alt={actor.name} className="single-actor-photo" src={actor.photo_url} />
              </div>
              <div className='single-actor-heading'>
                <h4>
                  {actor.name}
                </h4>
              </div>
              <div className='single-actor-bio'>
                <div>
                <p>{actor.bio?.length < 800 ? actor.bio : actor.bio ? actor.bio?.slice(0, 800 + actor["bio"].slice(800).indexOf(" ")) + " ..." : null}</p>
                </div>
                <div>
                <p><b>Born:</b> {actor["date_of_birth"]} in {actor["place_of_birth"]}</p>
                <div className='single-actor-options'>
                  <Link className="edit-actor-link" to={`/actors/${actor.id}/edit`}>Edit Actor</Link>
                  &emsp;
                  <div className="delete-actor-link" onClick={() => setShowModal(true)}>Delete Actor</div>
                </div>
              </div>
              </div>
            </div>

        : null}
        <div className='single-actor-filmography'>
          <table className='filmography-table'>
            <thead>
            <tr>
              <td>
              <h4>
              Filmography
            </h4>
              </td>
            </tr>
            </thead>
            <tbody>
              {actor?.filmography.map((film, idx) => {
                return (
                <tr className='filmography-row' key={`filmography-row-${idx}`}>
                  <td className='filmography-title'>
                    <Link to={`/films/${film.id}`}>{film.title}</Link>
                  </td>
                  <td className='filmography-year'>
                    {film.year}
                  </td>
                </tr>
                )
              })}
            </tbody>
          </table>
        </div>
        <DeleteActorModal showModal={showModal} setShowModal={setShowModal} name={actor?.name} id={actor?.id} />
      </div>
    )  
  } else {
    return null;
  }
};


export default SingleActor;