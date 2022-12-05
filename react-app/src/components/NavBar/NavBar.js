import { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";

function Navbar () {
  const [searchParams, setSearchParams] = useState("");
  const [films, setFilms] = useState([]);
  const [actors, setActors] = useState([]);
  const [matches, setMatches] = useState([]);
  const [selectedSearch, setSelectedSearch] = useState(null);
  const [hover, setHover] = useState(false);

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
        setSelectedSearch(matches[idx + 1]);
      }
    } else if (e.key === 'ArrowUp' && idx > 0) {
      setSelectedSearch(matches[idx - 1]);
    }
  };
  
  const handleSearch = e => {
    const params = e.target.value
    setSearchParams(params);
    const results = [];
    console.log(searchParams);
    console.log(params);
    for (let i = 0; i < actors.length; i++) {
      if (actors[i].name.toLowerCase().includes(params.toLowerCase())) {
        results.push(actors[i]);
      }
    };
    for (let i = 0; i < films.length; i++) {
      if (films[i].title.toLowerCase().includes(params.toLowerCase())) {
        results.push(films[i]);
      }
    }
    setMatches(results);
    setSelectedSearch(results[0]);
  };

  return (
    <div className="navbar">
      <div className="navbar-logo">

      </div>
      <div className="navbar-search">
        <form className="nav-search-form">
          <div>
            <input
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
                return <li>
                  {result.label}
                </li>
              }
              return (
                <li
                  className={selectedSearch === result ? "search-dropdown-selected" : null}
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