import React, { Component } from 'react';

import './App.css';
import 'semantic-ui-css/semantic.min.css'

import Map from './components/Map';
import Dashboard from './components/Dashboard';

import store from "./store/index";
import {UPDATE_PREDICTIONS} from "./actions/action-types";

import axios from 'axios';

class App extends Component {

  constructor() {
    super();

    let appState = store.getState();

    this.state = {
      country: appState.country,
      predictions: appState.predictions,

    };
  }

  updatePredictions = () => {

    let context = this;

    console.log('updating predictions');
    axios
      .get('http://localhost:5000/prediction/live?country=' + this.state.country.name.toLowerCase())
      .then(res => {

        console.log('from API');
        console.log(res.data.predictions);

        store.dispatch({
          type: UPDATE_PREDICTIONS,
          payload: res.data.predictions
        });

        let appState = store.getState();
        let currState = context.state;
        currState.predictions = appState.predictions;
        context.setState(currState);

        console.log('curr app state');
        console.log(context.state);
      });
  };

  componentDidMount() {
    this.updateMapPosition();
    this.updatePredictions();
  }

  updateMapPosition = () => {
    let appState = store.getState();
    let currState = this.state;
    currState.country = appState.country;
    this.setState(currState);
  };

  render() {

    return (
      <div className="App">
        <Map predictions={this.state.predictions}/>
        <Dashboard countryChanged={this.updateMapPosition} />
      </div>
    );
  }
}

export default App;
