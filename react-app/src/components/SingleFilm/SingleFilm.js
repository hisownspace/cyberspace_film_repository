import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import NotFound from "../NotFound";

function SingleFilm () {
  const filmId = useParams().id
  const [loaded, setLoaded] = useState(false);
  const [errors, setErrors] = useState(false)

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/films/${filmId}`);
      if (res.ok) {
        const film = await res.json();
      } else {
        console.log(res.status);
        setErrors(res.status);
      }
    })().then(setLoaded(true));
    return setLoaded(false);
  }, [filmId]);

  if (errors) {
    return <NotFound />
  } else if (loaded) {
    return (
      <>
        <h1>One Film!!!!!!!!</h1>
      </>
    )
  } else {
    return null;
  }

};

export default SingleFilm;