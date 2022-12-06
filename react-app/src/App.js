import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Actors from "./components/Actors";
import Films from "./components/Films";
import AddActor from "./components/AddActor";
import SingleActor from './components/SingleActor';
import SingleFilm from './components/SingleFilm';
import EditActor from './components/EditActor';
import AddFilm from './components/AddFilm';
import EditFilm from './components/EditFilm';
import Navbar from './components/NavBar';
import Splash from './components/Splash';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Switch>
        <Route path="/"><Splash /></Route>
        <Route path="/actors/add"><AddActor /></Route>
        <Route path="/actors/:id/edit"><EditActor /></Route>
        <Route path="/actors/:id"><SingleActor /></Route>
        <Route path="/actors"><Actors /></Route>
        <Route path="/films/add"><AddFilm /></Route>
        <Route path="/films/:id/edit"><EditFilm /></Route>
        <Route path="/films/:id"><SingleFilm /></Route>
        <Route path="/films"><Films /></Route>
      </Switch>

    </BrowserRouter>
  );
}

export default App;
