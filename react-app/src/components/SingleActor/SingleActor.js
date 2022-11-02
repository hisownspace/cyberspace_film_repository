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
        setActor(actor);
      } else {
        console.log(res.status);
        setErrors(res.status);
      };
    })().then(setLoaded(true));
    return () => setLoaded(false);
  }, [actorId]);

  if (errors) {
    return <NotFound />;
  } else if (loaded) {
    return (
      <>
        {actor ? 
        <div className='single-actor-main'>
          <ActorCard actor={actor[actorId]} />
        </div>
        : null}
      </>
    )  
  } else {
    return null;
  }
};


export default SingleActor;