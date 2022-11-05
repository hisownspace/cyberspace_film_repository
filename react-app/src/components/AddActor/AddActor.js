import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

function AddActor() {
  const [name, setName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [photoUrl, setPhotoUrl] = useState("");
  const [bio, setBio] = useState("");
  const [films, setFilms] = useState([]);;
  const [selectedFilms, setSelectedFilms] = useState([]);
  const [isChecked, setIsChecked] = useState(false);
  const [checkedState, setCheckedState] = useState([]);

  const history = useHistory();

  const changeCheck = () => {
    setIsChecked(!isChecked);
  }

  const handleCancel = e => {
    history.push("/");
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
          console.log(data.errors);
        }
      }
    })()
  }, []);

  useEffect(() => {
    console.log(films);
    console.log(checkedState);
  }, [films, checkedState])

  const handleSubmit = async e => {
    e.preventDefault();

    const actorForm = {
      name,
      "date_of_birth": dateOfBirth,
      "place_of_birth": placeOfBirth,
      "photo_url": photoUrl,
      bio
    };

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
    <div className="form-main">
      <h1 className="add-actor-header">
        Add An Actor!
      </h1>
      <form className="addActorForm" onSubmit={handleSubmit}>
        <div className="errors">

        </div>
        <label htmlFor="name">
          Name
        </label>
        <input
          id="name"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <p className="errors">

        </p>
        <label htmlFor="dateOfBirth">
          Date of Birth
        </label>
        <input
          type="date"
          id="dateOfBirth"
          value={dateOfBirth}
          onChange={e => setDateOfBirth(e.target.value)}
        />
        <p className="errors">

        </p>
        <label htmlFor="placeOfBirth">
          Place of Birth
        </label>
        <input
          id="placeOfBirth"
          value={placeOfBirth}
          onChange={e => setPlaceOfBirth(e.target.value)}
        />
        <p className="errors">

        </p>
        <label htmlFor="photo">
          Photo Url
        </label>
        <input
          id="photo"
          value={photoUrl}
          onChange={e => setPhotoUrl(e.target.value)}
        />
        <label htmlFor="bio">
          Biography
        </label>
        <textarea
          id="bio"
          value={bio}
          onChange={e => setBio(e.target.value)}
        />
        {films.map((film, idx) => {
          return (<>
          {film[0]} {film[1]} {film[2]}
          </>)
        })}

        <label htmlFor="checkers">
          Test
        </label>
        <input
          type="checkbox"
          id="checkers"
          name="checkers"
          value="test"
          checked={isChecked}
          onChange={changeCheck}
          />
        
        <div className="buttonHole">
          <button className="cancel" type="button" onClick={handleCancel}>Cancel</button>
          <button>Submit</button>
        </div>
      </form>
    </div>
  );
};

export default AddActor;