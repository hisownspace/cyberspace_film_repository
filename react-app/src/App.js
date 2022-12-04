import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Actors from "./components/Actors";
import Films from "./components/Films";
import AddActor from "./components/AddActor";
import SingleActor from './components/SingleActor';
import SingleFilm from './components/SingleFilm';
import EditActor from './components/EditActor';
import AddFilm from './components/AddFilm';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/actors/add"><AddActor /></Route>
        <Route path="/actors/:id/edit"><EditActor /></Route>
        <Route path="/actors/:id"><SingleActor /></Route>
        <Route path="/actors"><Actors /></Route>
        <Route path="/films/add"><AddFilm /></Route>
        <Route path="/films/:id"><SingleFilm /></Route>
        <Route path="/films"><Films /></Route>
      </Switch>

    </BrowserRouter>
  );
}

export default App;
