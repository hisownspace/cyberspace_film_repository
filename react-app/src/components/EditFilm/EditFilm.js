import { useState, useEffect } from "react";
import { useParams, useHistory } from "react-router-dom";


const EditFilm = () => {
  const [title, setTitle] = useState("");
  const [year, setYear] = useState(1902);
  const [plot, setPlot] = useState("");
  const [photoUrl, setPhotoUrl] = useState("");
  const [genreId, setGenreId] = useState("");
  const [genres, setGenres] = useState([]);
  const [actors, setActors] = useState([]);
  const [castSearch, setCastSearch] = useState([]);
  const [cast, setCast] = useState([]);
  const [matches, setMatches] = useState([]);
  const [selectedSearch, setSelectedSearch] = useState(null);
  const [hover, setHover] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [errors, setErrors] = useState({});

  const { id } = useParams();

  const history = useHistory();

  const handleCancel = e => {
    history.push(`/films/${id}`);
  };

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/films/${id}`);
      const data = await res.json();
      if (res.ok) {
        document.title = `Edit ${data.title}`;
        setTitle(data.title);
        setYear(data.year);
        setPlot(data.plot);
        setPhotoUrl(data["photo_url"]);
        setGenreId(data.genre.id);
        setCast(data.cast);
      } else {
        console.log(data.errors);
      };
    })()
  }, [id]);

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/actors/");
      if (res.ok) {
        const data = await res.json();
        console.log(Object.values(data));
        setActors(Object.values(data));
      } else {
        const data = await res.json();
        if (data.errors) {
          setErrors(data.errors);
          console.log(data.errors);
        };
        // setSubmitted(true);
      };
    })();
  }, []);

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/genres/");
      const data = await res.json();
      if (res.ok) {
        console.log(data);
        setGenres(data);
      } else {
        if (data.errors) {
          setErrors(data.errors);
          console.log(data.errors);
        };
        // setSubmitted(true);
      };
    })();
  }, []);

  const clearSearch = () => {
    setMatches([]);
    // setCastSearch("");
  };

  const searchActors = e => {
    const castNames = [];
    for (let i = 0; i < cast.length; i++) {
      castNames.push(cast[i].name);
    };
    const actorNames = [];
    for (let i = 0; i < actors.length; i++) {
      actorNames.push(actors[i].name);
    };
    const param = e.target.value;
    setCastSearch(param);
    const nameMatches = [];
    for (let i = 0; i < actors.length; i++) {
      const name = actors[i].name.toLowerCase()
      console.log(name)
      console.log(cast.indexOf(actors[i]));

      if (name.includes(param.toLowerCase()) && !castNames.includes(actorNames[i])) {
        nameMatches.push(actors[i]);
      };
    };
    if (param.length) {
    setMatches(nameMatches);
    setSelectedSearch(nameMatches[0]);
    } else {
      setMatches([]);
    }
  };

  const addToCast = actor => {
    const tempCast = [ ...cast ];
    tempCast.push(actor);
    setCast(tempCast);
    setCastSearch("");
    setMatches([]);
    setHover(false);
  };

  const removeFromCast = actor => {
    const newCast = cast.filter(elem => elem !== actor);
    setCast(newCast);
  };

  const toggleClass = (e, action) => {
    if (action === "enter") {
    e.target.parentElement.className = "cast-member-hover";
    } else {
    e.target.parentElement.className = "cast-member";
    }
  };

  const handleKeyPress = e => {
    const idx = matches.indexOf(selectedSearch);
    if (matches.length === 0) {
      return;
    } else if (e.key === 'Enter') {
      e.preventDefault();
      addToCast(selectedSearch);
    } else if (hover) {
      return; 
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (idx >= 0 && idx < matches.length - 1) {
        setSelectedSearch(matches[idx + 1]);
      }
    } else if (e.key === 'ArrowUp' && idx > 0) {
      setSelectedSearch(matches[idx - 1]);
    }
  };

  const handleSubmit = async e => {
    e.preventDefault();

    const castIds = [];
    for (let i = 0; i < cast.length; i++) {
      castIds.push(cast[i].id.toString());
    };
    console.log(castIds);

    const filmForm = {
      title,
      year,
      plot,
      "photo_url": photoUrl,
      "genre_id": genreId,
      castIds: JSON.stringify(castIds)
    }

    console.log(JSON.stringify(filmForm))

    const res = await fetch (`/api/films/${id}`,
      {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(filmForm)
      }
    );
    setSubmitted(true);
    const data = await res.json();
    if (res.ok) {
      // const film = await res.json();
      const film = data;
      history.push(`/films/${film.id}`)
    } else if (data.errors) {
      console.log(res.status);
      // const data = await res.json();
      // if (data.errors) {
      setErrors(data.errors);
      console.log(data.errors);
      // }
    } else {
      setErrors(["Unknown Error!"])
    }
  }
  return (
    <div className="form-main">
      <h1 className="add-actor-header">
        Edit {title}
      </h1>
      <form className="addActorForm" onSubmit={handleSubmit}>
        <div className="errors">
          {errors.title && submitted ? "Title: " + errors.title : null}
        </div>
        <label
          htmlFor="title"
          className="actor-label"
        >
          Title
        </label>
        <input
          className="actor-input"
          id="title"
          value={title}
          onChange={e => setTitle(e.target.value)}
        />
        <p className="errors">
          {errors.year && submitted ? "Year: " + errors.year : null}
        </p>
        <label
          htmlFor="year"
          className="actor-label"
        >
          Year
        </label>
        <input
          className="actor-input"
          type="number"
          id="year"
          value={year}
          onChange={e => setYear(e.target.value)}
        />
        <p className="errors">
          {errors.plot && submitted ? "Plot:" + errors.plot[0] : null}
        </p>
        <label
          htmlFor="plot"
          className="actor-label"
        >
          Plot
        </label>
        <textarea
          id="plot"
          value={plot}
          onChange={e => setPlot(e.target.value)}
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
          {errors.genre_id && submitted ? "Genre ID: Please Select A Genre" : null}
        </p>
        <label
          htmlFor="genreId"
          className="actor-label"
        >
          Genre
        </label>
        <select
          className="actor-input"
          id="genreId"
          value={genreId}
          onChange={e => setGenreId(e.target.value)}
        >
        <option disabled>-- Please Select a Genre --</option>
        {genres.map((genre, idx) => {
          return <option key={idx} value={genre[0]}>{genre[1]}</option>
        })}
        </select>
        <label
          htmlFor="cast"
          className="actor-label"
        >
          Cast
        </label>
        <input
          className="actor-input search-box"
          id="cast"
          value={castSearch}
          onChange={searchActors}
          onBlur={clearSearch}
          onFocus={searchActors}
          onKeyDown={handleKeyPress}
        />
        {matches.length ? <ul onMouseDown={e => e.preventDefault()}className="search-dropdown">
        {matches.map(actor => {
          return (
            <li
              key={actor.id}
              className={selectedSearch === actor ? "search-dropdown-selected" : null}
              onClick={() => addToCast(actor)}
              onMouseOver={() => {setSelectedSearch(actor); setHover(true)}}
              onMouseLeave={() => setHover(false)}
            >
              {actor.name}
            </li>
          )
        })
        }
        </ul> : null}
        <div className="cast-list">
          {cast.map(actor => {
            return (
              <span key={actor.name} className="cast-member">
                {actor.name}&ensp;&nbsp;<b
                  className="remove-cast-member"
                  onMouseOver={e => toggleClass(e, "enter")}
                  onMouseLeave={e => toggleClass(e, "leave")}
                  onClick={() => removeFromCast(actor)}
                  >x</b>
              </span>
            )
          })}
        </div>
        <div className="buttonHole" id="search-allowance-buttons">
          <button className="cancel" type="button" onClick={handleCancel}>Cancel</button>
          <button>Submit</button>
        </div>
      </form>
    </div>
  );
};

export default EditFilm;