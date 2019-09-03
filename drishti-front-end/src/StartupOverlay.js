import React, { Component } from 'react';
import { Button, Segment } from 'semantic-ui-react'

// routing
import { withRouter } from "react-router-dom";

class StartupOverlay extends Component {

  componentDidMount() {
    this.props.history.push({
      pathname: '/'
    });
  }

  goToApp = () => {
    this.props.history.push({
      pathname: '/app'
    });
  };

  render() {
    return (
      <div className="StartupOverlay" style={styles.overlay}>
        <div style={styles.box}>
          <div style={styles.boxTitle}>
            drishti
          </div>
          <div style={styles.subText}>
            predicts violence using information retrieval and machine learning
          </div>
          <Segment inverted>
            <Button
              inverted color='green'
              content={'Get Started'}
              onClick={() => this.goToApp()}
            />
          </Segment>
        </div>
      </div>
    );
  }
}

const styles = {
  overlay: {
    // fontFamily: 'Titillium Web'
    width: '100vw',
    height: '100vh',
    backgroundColor: '#1b1c1d',
    opacity: 0.9,
  },
  box: {
    position: 'absolute',
    width: '100vw',
    textAlign: 'center',
    top: '30vh'
  },
  boxTitle: {
    fontSize: '96px',
    fontWeight: 500,
    color: '#B0DDD9',
  },
  subText: {
    fontSize: '24px',
    fontWeight: 300,
    color: '#fff',
    marginTop: '10vh',
    marginBottom: '5vh',
  }
};

export default withRouter(StartupOverlay);
