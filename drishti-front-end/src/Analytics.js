import React, { Component } from 'react';
import { Button, Segment } from 'semantic-ui-react'

// routing
import { withRouter } from "react-router-dom";

class Analytics extends Component {

  componentDidMount() {
    this.props.history.push({
      pathname: '/analytics'
    });
  }

  goToApp = () => {
    this.props.history.push({
      pathname: '/app'
    });
  };

  render() {

    const dashboard1 = '<script type=\'text/javascript\' src=\'https://us-east-1.online.tableau.com/javascripts/api/viz_v1.js\'></script><div class=\'tableauPlaceholder\' style=\'width: 1000px; height: 827px;\'><object class=\'tableauViz\' width=\'1000\' height=\'827\' style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fus-east-1.online.tableau.com%2F\' /> <param name=\'embed_code_version\' value=\'3\' /> <param name=\'site_root\' value=\'&#47;t&#47;sonal\' /><param name=\'name\' value=\'PredictionMetrics&#47;Dashboard1\' /><param name=\'tabs\' value=\'no\' /><param name=\'toolbar\' value=\'yes\' /><param name=\'showAppBanner\' value=\'false\' /><param name=\'filter\' value=\'iframeSizedToWindow=true\' /></object></div>';
    const dashboard2 = '<script type=\'text/javascript\' src=\'https://us-east-1.online.tableau.com/javascripts/api/viz_v1.js\'></script><div class=\'tableauPlaceholder\' style=\'width: 1000px; height: 827px;\'><object class=\'tableauViz\' width=\'1000\' height=\'827\' style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fus-east-1.online.tableau.com%2F\' /> <param name=\'embed_code_version\' value=\'3\' /> <param name=\'site_root\' value=\'&#47;t&#47;sonal\' /><param name=\'name\' value=\'LocationspercountryACLED&#47;Dashboard1\' /><param name=\'tabs\' value=\'no\' /><param name=\'toolbar\' value=\'yes\' /><param name=\'showAppBanner\' value=\'false\' /><param name=\'filter\' value=\'iframeSizedToWindow=true\' /></object></div>';
    const dashboard3 = '<script type=\'text/javascript\' src=\'https://us-east-1.online.tableau.com/javascripts/api/viz_v1.js\'></script><div class=\'tableauPlaceholder\' style=\'width: 1440px; height: 640px;\'><object class=\'tableauViz\' width=\'1440\' height=\'640\' style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fus-east-1.online.tableau.com%2F\' /> <param name=\'embed_code_version\' value=\'3\' /> <param name=\'site_root\' value=\'&#47;t&#47;sonal\' /><param name=\'name\' value=\'SentimentVsLabel&#47;Sheet1\' /><param name=\'tabs\' value=\'no\' /><param name=\'toolbar\' value=\'yes\' /><param name=\'showAppBanner\' value=\'false\' /><param name=\'filter\' value=\'iframeSizedToWindow=true\' /></object></div>';

    return (
      <div className="Analytics" style={styles.overlay}>
        <div style={styles.box}>
          <div style={styles.boxTitle}>
            analytics
          </div>
          <div style={styles.btn}>
            <Button
              inverted color='green'
              content={'Go Back'}
              onClick={() => this.goToApp()}
            />
          </div>

          <div contentEditable='true' dangerouslySetInnerHTML={{ __html: dashboard1 }}></div>
          <div contentEditable='true' dangerouslySetInnerHTML={{ __html: dashboard2 }}></div>
          <div contentEditable='true' dangerouslySetInnerHTML={{ __html: dashboard3 }}></div>

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
    backgroundColor: '#fff',
    opacity: 0.9,
  },
  box: {
    // position: 'absolute',
    width: '96vw',
    textAlign: 'left',
    padding: '2vw',
    // top: '2vw'
  },
  boxTitle: {
    fontSize: '52px',
    fontWeight: 500,
    color: '#B0DDD9',
  },
  subText: {
    fontSize: '24px',
    fontWeight: 300,
    color: '#fff',
    marginTop: '10vh',
    marginBottom: '5vh',
  },
  btn: {
    marginTop: '4vh',
    marginBottom: '2vh',
  }
};

export default withRouter(Analytics);
