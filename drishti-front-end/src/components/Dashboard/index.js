import React, { Component } from 'react';
import { Dropdown } from 'semantic-ui-react'
import { Button, Segment } from 'semantic-ui-react'

import {COUNTRY} from "../../constants/index";
import store from "../../store/index";


import {UPDATE_COUNTRY} from "../../actions/action-types";

// routing
import { withRouter } from "react-router-dom";

const countryOptions = [
  { key: COUNTRY.INDIA.code, value: COUNTRY.INDIA.code, flag: COUNTRY.INDIA.code, text: COUNTRY.INDIA.name },
  { key: COUNTRY.THAILAND.code, value: COUNTRY.THAILAND.code, flag: COUNTRY.THAILAND.code, text: COUNTRY.THAILAND.name },
  { key: COUNTRY.INDONESIA.code, value: COUNTRY.INDONESIA.code, flag: COUNTRY.INDONESIA.code, text: COUNTRY.INDONESIA.name },
];


class Dashboard extends Component {

  constructor() {
    super();

    let appState = store.getState();

    this.state = {
      countryVal: appState.country.code
    };

  }

  goToAnalytics = () => {
    this.props.history.push({
      pathname: '/analytics'
    });
  };

  onChange = (e, data) => {

    let currState = this.state;
    currState.countryVal = data.value;
    this.setState(currState);

    // make change in store
    if (data.value === COUNTRY.INDIA.code) {
      store.dispatch({
        type: UPDATE_COUNTRY,
        payload: {
          country: COUNTRY.INDIA
        }
      });
    } else if (data.value === COUNTRY.THAILAND.code) {
      store.dispatch({
        type: UPDATE_COUNTRY,
        payload: {
          country: COUNTRY.THAILAND
        }
      });
    } else if (data.value === COUNTRY.INDONESIA.code) {
      store.dispatch({
        type: UPDATE_COUNTRY,
        payload: {
          country: COUNTRY.INDONESIA
        }
      });
    }

    this.props.history.push({
      pathname: '/refresh'
    });

    // this.props.countryChanged();
  };


  render() {
    return (
      <div className="DashboardContainer" style={styles.container}>

        <div style={styles.content}>
          <div style={styles.heading}>
            Country
          </div>
          <div className="country-dropdown" style={styles.countryDropDown}>
            <Dropdown
              placeholder='Select Country'
              fluid
              search
              selection
              options={countryOptions}
              defaultValue={this.state.countryVal}
              onChange={this.onChange}
            />

            <Segment inverted>
              <Button
                inverted color='green'
                onClick={() => this.goToAnalytics()}
                content={'Go to Analysis'}
              />

            </Segment>

          </div>
        </div>
      </div>
    );
  }
}

const styles = {
  container: {
    height: '100vh',
    width: '25vw',
    backgroundColor: '#193341',
    backgroundColor: '#1b1c1d',
    position: 'absolute',
    top: 0,
    right: 0,


  },
  content: {
    margin: '5%',
    color: '#fff',
  },
  heading: {
    fontSize: '30px',
    fontWeight: '500',
    textAlign: 'left',

  },
  countryDropDown: {
    marginTop: '20px'
  }
};

export default withRouter(Dashboard);
