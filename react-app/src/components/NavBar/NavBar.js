import { useEffect, useState, useRef } from "react";
import { Link, useHistory } from "react-router-dom";

function Navbar () {
  const [searchParams, setSearchParams] = useState("");
  const [films, setFilms] = useState([]);
  const [actors, setActors] = useState([]);
  const [matches, setMatches] = useState([]);
  const [selectedSearch, setSelectedSearch] = useState(null);
  const [hover, setHover] = useState(false);

  const searchInput = useRef(null);
  const history = useHistory();

  useEffect(() => {
    (async () => {
      const filmRes = await fetch('/api/films/');
      const actorRes = await fetch('/api/actors/');
      const actors = await actorRes.json();
      const films = await filmRes.json();
      if (filmRes.ok && actorRes.ok) {
        setActors(Object.values(actors));
        setFilms(Object.values(films));
      } else {
        console.log(actors.errors);
        console.log(films.errors);
      }
    })()
  }, []);

  const goToPage = result => {
    setMatches([]);
    searchInput.current.blur();
    if (result.title) {
      history.push(`/films/${result.id}`);
    } else {
      history.push(`/actors/${result.id}`);
    }
  };

  const handleKeyPress = e => {
    const idx = matches.indexOf(selectedSearch);
    if (matches.length === 0) {
      return;
    } else if (e.key === 'Enter') {
      e.preventDefault();
      goToPage(selectedSearch);
    } else if (hover) {
      return; 
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (idx >= 0 && idx < matches.length - 1) {
        if (matches[idx + 1].isCategory) {
          if (matches[idx + 2]) setSelectedSearch(matches[idx + 2]);
        } else {
          setSelectedSearch(matches[idx + 1]);
        }
      }
    } else if (e.key === 'ArrowUp' && idx > 1) {
      if (matches[idx - 1].isCategory) {
        if (matches[idx - 2] && !matches[idx - 2].isCategory) setSelectedSearch(matches[idx - 2]);
      } else {
        setSelectedSearch(matches[idx - 1]);
      }
    }
  };
  
  const handleSearch = e => {
    const params = e.target.value
    setSearchParams(params);
    const actorCat = { isCategory: true, label: "Actors" };
    const results = [actorCat];
    console.log(searchParams);
    console.log(params);
    for (let i = 0; i < actors.length; i++) {
      if (actors[i].name.toLowerCase().includes(params.toLowerCase())) {
        results.push(actors[i]);
      }
    };
    const movieCat = { isCategory: true, label: "Movies" };
    results.push(movieCat);
    for (let i = 0; i < films.length; i++) {
      if (films[i].title.toLowerCase().includes(params.toLowerCase())) {
        results.push(films[i]);
      }
    }
    setMatches(results);
    if (!results[1].isCategory) {
      setSelectedSearch(results[1]);
    } else {
      setSelectedSearch(results[2]);
    }
  };

  return (
    <div className="navbar">
      <div className="navbar-logo">

      </div>
      <div className="navbar-search">
        <form className="nav-search-form">
          <div>
            <input
              ref={searchInput}
              className="nav-search-input"
              value={searchParams}
              onChange={handleSearch}
              onBlur={() => setMatches([])}
              onFocus={handleSearch}
              onKeyDown={handleKeyPress}
            />
            {matches.length ? <ul onMouseDown={e => e.preventDefault()} className="navbar-search-dropdown">
            {matches.map(result => {
              if (result.isCategory) {
                return <li className="search-categories">
                  {result.label}
                </li>
              }
              return (
                <li
                  className={selectedSearch === result ? "search-dropdown-selected search-li" : "search-li"}
                  onClick={() => goToPage(result)}
                  onMouseOver={() => {setSelectedSearch(result); setHover(true)}}
                  onMouseLeave={() => setHover(false)}
                >
                  {result.name || result.title}
                </li>
              )
            })
            }
            </ul> : null}
            <button>Submit</button>
          </div>
        </form>
      </div>
      <div className="navbar-profile">

      </div>
    </div>
  )
};

export default Navbar;