import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

function AddActor() {
  const [name, setName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [photoUrl, setPhotoUrl] = useState("");
  const [bio, setBio] = useState("");
  const [films, setFilms] = useState([]);;
  const [checkedState, setCheckedState] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [errors, setErrors] = useState({});

  const history = useHistory();

const handleCheckedState = (e, idx) => {
  const tempCheckedState = [...checkedState];
  tempCheckedState[idx] = !tempCheckedState[idx];
  setCheckedState(tempCheckedState);
};

  const handleCancel = e => {
    history.push("/");
  }

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/films/");
      if (res.ok) {
        const data = await res.json();
        console.log(Object.values(data));
        setFilms(Object.values(data));
        setCheckedState(new Array(Object.values(data).length).fill(false));
      } else {
        const data = await res.json();
        if (data.errors) {
          setErrors(data.errors);
          console.log(data.errors);
        }
        setSubmitted(true);
      }
    })()
  }, []);

   const handleSubmit = async e => {
    e.preventDefault();

    const filmography = [];

    for (let i = 0; i < films.length; i++) {
      if (checkedState[i]) {
        filmography.push(films[i].id);
      }
    }

    const actorForm = {
      name,
      "date_of_birth": dateOfBirth,
      "place_of_birth": placeOfBirth,
      "photo_url": photoUrl,
      bio,
      filmography
    };

    const res = await fetch("/api/actors/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(actorForm)
      });
    setSubmitted(true);
    if (res.ok) {
      const actor = await res.json();
      history.push(`/actors/${actor.id}`);
    } else {
      console.log(res.status);
      const data = await res.json();
      if (data.errors) {
        setErrors(data.errors);
        console.log(data.errors);
      }
    }
  }

  return (
    <div className="form-main">
      <h1 className="add-actor-header">
        Add An Actor!
      </h1>
      <form className="addActorForm" onSubmit={handleSubmit}>
        <div className="errors">
          {errors.name && submitted ? "Name: " + errors.name[0] : null}
        </div>
        <label
          htmlFor="name"
          className="actor-label"
        >
          Name
        </label>
        <input
          className="actor-input"
          id="name"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <p className="errors">
          {errors.date_of_birth && submitted ? "Date of birth: " + errors.date_of_birth[0] : null}
        </p>
        <label
          htmlFor="dateOfBirth"
          className="actor-label"
        >
          Date of Birth
        </label>
        <input
          className="actor-input"
          type="date"
          id="dateOfBirth"
          value={dateOfBirth}
          onChange={e => setDateOfBirth(e.target.value)}
        />
        <p className="errors">
          {errors.place_of_birth && submitted ? "Place of Birth: " + errors.place_of_birth : null}
        </p>
        <label
          htmlFor="placeOfBirth"
          className="actor-label"
        >
          Place of Birth
        </label>
        <input
          className="actor-input"
          id="placeOfBirth"
          value={placeOfBirth}
          onChange={e => setPlaceOfBirth(e.target.value)}
        />
        <p className="errors">
          {errors.photo_url && submitted ? "Photo URL: " + errors.photo_url : null}
        </p>
        <label
          htmlFor="photo"
          className="actor-label"
        >
          Photo URL
        </label>
        <input
          className="actor-input"
          id="photo"
          value={photoUrl}
          onChange={e => setPhotoUrl(e.target.value)}
        />
        <p className="errors">
          {errors.bio && submitted ? "Biography: " + errors.bio : null}
        </p>
        <label
          htmlFor="bio"
          className="actor-label"
        >
          Biography
        </label>
        <textarea
          id="bio"
          value={bio}
          onChange={e => setBio(e.target.value)}
        />
        <ul>
        {films.map((film, idx) => {
          return (
            <li
              key={`film-checkbox-div-${film.id}`}
              className="checkbox-div"
            >
              <label
                className="checkbox-label"
                htmlFor={`film-checkbox-${film.id}`}
                key={`film-checkbox-label-${film.id}`}  
              >
                {film.title}
              </label>
              <input
                type="checkbox"
                key={`film-checkbox-${film.id}`}
                id={`film-checkbox-${film.id}`}
                name={film.title}
                value={film.title}
                checked={checkedState[idx] === undefined ? false : checkedState[idx]}
                onChange={e => handleCheckedState(e, idx)}
              />  
            </li>
          )
        })}
        </ul>
        <div className="buttonHole">
          <button className="cancel" type="button" onClick={handleCancel}>Cancel</button>
          <button>Submit</button>
        </div>
      </form>
    </div>
  );
};

export default AddActor;