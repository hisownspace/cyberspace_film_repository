import { useEffect, useState } from "react";
import { useHistory, useParams } from "react-router-dom";

function EditActor() {
  const [name, setName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [photoUrl, setPhotoUrl] = useState("");
  const [bio, setBio] = useState("");
  const [films, setFilms] = useState([]);
  const [checkedState, setCheckedState] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [errors, setErrors] = useState({});
  let { id } = useParams();

  const history = useHistory();

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/actors/${id}`);

      if (res.ok) {

        const data = await res.json();
        const actor = data;
        document.title = `Edit ${actor.name}`;
        setName(actor.name);
        let dob = new Date(actor.date_of_birth);
        // const year = dob.toLocaleString("default", { year: "numeric" });
        // const month = dob.toLocaleString("default", { month: "2-digit" })
        // const day = dob.toLocaleString("default", { day: "2-digit" });
        // dob = year + "-" + month + "-" + day;
        dob = dob.toISOString().split("T")[0];
        setDateOfBirth(dob);
        setPlaceOfBirth(actor.place_of_birth);
        setPhotoUrl(actor.photo_url);
        setBio(actor.bio);
        const tempChecked = new Array(films.length).fill(false);
        for (let i = 0; i < actor.filmography.length; i++) {
          const found = films?.findIndex(film => film.id === actor.filmography[i].id);
          if (found >= 0) {
            tempChecked[found] = true;
          }
        }        
        setCheckedState(tempChecked);
      }
    }
    )()
    setLoaded(true);
  }, [id, films, dateOfBirth]);

  const handleCheckedState = (e, idx) => {
    const tempCheckedState = [...checkedState];
    tempCheckedState[idx] = !tempCheckedState[idx];
    setCheckedState(tempCheckedState);
  };

  const handleCancel = e => {
    history.push(`/actors/${id}`);
  }

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/films/");
      if (res.ok) {
        const data = await res.json();
        setFilms(Object.values(data));
        setCheckedState(new Array(Object.values(data).length).fill(false));
      } else {
        const data = await res.json();
        if (data.errors) {
          setErrors(data.errors);
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


    const res = await fetch(`/api/actors/${id}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(actorForm)
      });

    if (res.ok) {
      const actor = await res.json();
      history.push(`/actors/${actor.id}`);
    } else {
      const data = await res.json();
      if (data.errors) {
        setErrors(data.errors);
      }
    }
  }

  return (
    loaded ? <div className="form-main">
      <h1 className="add-actor-header">
        Edit {name}!
      </h1>
      <form className="addActorForm" onSubmit={handleSubmit}>
        <div className="errors">
          {errors.name? errors.name : null}
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
          {errors.date_of_birth ? errors.date_of_birth : null}
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
          {errors.place_of_birth ? errors.place_of_birth : null}
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
          {errors.photo_url ? errors.photo_url : null}
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
          {errors.bio ? errors.bio : null}
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
    </div> : null
  );
};

export default EditActor;