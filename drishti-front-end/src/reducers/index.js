import {FOO_IT, UPDATE_COUNTRY, UPDATE_PREDICTIONS} from "../actions/action-types";
import {COUNTRY} from '../constants';

const initialState = {
  country: COUNTRY.INDIA,
  predictions: {

  }
};

export default function rootReducer(state = initialState, action) {

  if (action.type === UPDATE_COUNTRY) {
    state.country = action.payload.country;
    return state;
  }

  if (action.type === UPDATE_PREDICTIONS) {

    state.predictions = action.payload;

    console.log('updating store with predictions');
    console.log(action.payload);

    console.log('updated store with predictions');
    console.log(state);

    return state;
  }

  return state;
}