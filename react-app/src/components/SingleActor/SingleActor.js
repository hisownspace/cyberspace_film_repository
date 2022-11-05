import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import ActorCard from '../ActorCard';
import NotFound from '../NotFound';

const SingleActor = () => {
  const [loaded, setLoaded] = useState(false);
  const [actor, setActor] = useState();
  const [errors, setErrors] = useState(false)

  const actorId = useParams().id;


  
  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/actors/${actorId}`);
      if (res.ok) {
        const actor = await res.json();
        setActor(actor[actorId]);
      } else {
        setErrors(res.status);
      };
    })().then(setLoaded(true));
    return () => setLoaded(false);
  }, [actorId]);

  if (errors) {
    return <NotFound />;
  } else if (loaded) {
    return (
      <div className='single-actor-main'>
        {actor ? 
            <div className='single-actor-focus'>
              <div className="single-actor-photo-container">
                <img className="single-actor-photo" src={actor.photo_url}></img>
              </div>
              <div className='single-actor-heading'>
                <p>
                  {actor.name}
                </p>
              </div>
              <div className='single-actor-bio'>
                <div>
                <p>{actor["bio"]}</p>
                </div>
                <div>
                <p>Born: {actor["date_of_birth"]} in {actor["place_of_birth"]}</p>
                <p>
                  <a className="edit-actor-link" href="/actors/edit">Edit Actor</a>
                  &emsp;
                  <a className="edit-actor-link" href="/actors/delete">Delete Actor</a>
                </p>
              </div>
              </div>
            </div>
        : null}
      </div>
    )  
  } else {
    return null;
  }
};


export default SingleActor;