import { useHistory } from "react-router-dom";

function ActorCard ({ actor }) {
const history = useHistory();

  return(
    <div className="actor-card" onClick={() => history.push(`/actors/${actor.id}`)}>
      <div className="actor-card-image-container">
        <img
          className="actor-card-photo"
          src={actor.photo_url}
          alt={actor.name}
        />
      </div>
      <p
        className="actor-card-name">
        {actor.name}
        </p>
    </div>

  )
};

export default ActorCard;