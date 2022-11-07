import { useEffect, useState } from "react";
import { useHistory, useParams } from "react-router-dom";

function EditActor() {
  const [name, setName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [photoUrl, setPhotoUrl] = useState("");
  const [bio, setBio] = useState("");
  const [films, setFilms] = useState([]);;
  const [selectedFilms, setSelectedFilms] = useState([]);
  const [checkedState, setCheckedState] = useState([]);
  const [loaded, setLoaded] = useState(false);
  let { id } = useParams();

  const history = useHistory();

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/actors/${id}`);
      if (res.ok) {

        const data = await res.json();
        const actor = data[id];
        setName(actor.name);
        setDateOfBirth(actor.date_of_birth);
        setPlaceOfBirth(actor.place_of_birth);
        setPhotoUrl(actor.photo_url);
        setBio(actor.bio);
        console.log(actor.filmography);
        setFilms(actor.filmography);
      }
    }
    )().then(setLoaded(true));
  }, [id]);

  const handleCheckedState = (e, idx) => {
    const tempCheckedState = checkedState;
    tempCheckedState[idx] = !tempCheckedState[idx];
    setCheckedState(tempCheckedState);
    console.log(checkedState);
  };

  const handleCancel = e => {
    history.push(`/actors/${id}`);
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
          console.log(data.errors);
        }
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

    console.log(actorForm);

    const res = await fetch("/api/actors",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(actorForm)
      });

    if (res.ok) {
      const actor = await res.json();
      history.push(`/actors/${actor.id}`);
    } else {
      console.log(res.status);
      const data = await res.json();
      if (data.errors) {
        console.log(data.errors);
      }
    }
  }

  const addFilm = (e, idx) => {
    console.log("YOU CLICKED THE FUCKING BUTTON!!!!!");
    const tempFilms = selectedFilms;
    console.log(selectedFilms[idx]);
    console.log("FUCK", e.target.value)
    selectedFilms[idx] = !selectedFilms[idx];
    console.log(films);
    setSelectedFilms(tempFilms);
  };

  return (
    loaded ? <div className="form-main">
      <h1 className="add-actor-header">
        Edit {name}!
      </h1>
      <form className="addActorForm" onSubmit={handleSubmit}>
        <div className="errors">

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

        </p>
        <label
          htmlFor="photo"
          className="actor-label"
        >
          Photo Url
        </label>
        <input
          className="actor-input"
          id="photo"
          value={photoUrl}
          onChange={e => setPhotoUrl(e.target.value)}
        />
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
                // checked={checkedState[idx]}
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
    </div> : null
  );
};

export default EditActor;