import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Actors from "./components/Actors";
import Films from "./components/Films";
import AddActor from "./components/AddActor";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/actors"><Actors /></Route>
        <Route path="/films"><Films /> </Route>
        <Route path="/add-actor"><AddActor /></Route>
      </Switch>

    </BrowserRouter>
  );
}

export default App;
