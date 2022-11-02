

function ActorCard ({ actor }) {




  return(
    <>
      <h1>ACTOR CARD!!!!!</h1>
      <p>{actor.name}</p>
      <p>{actor.date_of_birth}</p>
      <p>{actor.place_of_birth}</p>
      {actor.filmography.map((elem, idx) => {
        return (<a href={`/films/${elem.id}`} key={idx}>{elem.title}</a>)
      })}
    </>

  )
};

export default ActorCard;