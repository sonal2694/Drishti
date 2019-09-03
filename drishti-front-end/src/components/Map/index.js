import React, { Component } from 'react';

import GoogleMapReact, { Marker} from 'google-map-react';
import MapStyle from './mapDarkStyle';
import MarkedArea from './MarkedArea';

import Config from '../../config';

import store from '../../store';


class Map extends Component {

  constructor(props) {
    super(props);

    let appState = store.getState();

    console.log("Maps constructor");
    console.log(appState.country);

    this.state = {
      center: {
        lat: appState.country.lat,
        lng: appState.country.long
      },
      zoom: appState.country.mapZoom,
      predictions: this.props.predictions
    };

  }

  handleApiLoaded = (map, maps) => {
    map.setOptions({
      styles: MapStyle,
      fullscreenControlOptions: {
        position: maps.ControlPosition.BOTTOM_RIGHT
      }
    });

  };

  render() {

    const items = [];

    for (let i = 0 ; i < this.props.predictions.length ; i++) {
      console.log(this.props.predictions[i]);

      let currColor = '';
      if (this.props.predictions[i].prediction === "NO_VIOLENCE") {
        console.log('color NO V');
        currColor = '#22BE34'
      }
      else if (this.props.predictions[i].prediction === "VIOLENCE") {
        console.log('color V');
        currColor = '#ff1744'
      }

      items.push(
        <MarkedArea
          locationName={this.props.predictions[i].location.name}
          lat={this.props.predictions[i].location.lat}
          lng={this.props.predictions[i].location.long}
          size={15}
          intensity={1}
          color={currColor}
        />
      )


    }

    return (
      <div className="MapContainer" style={styles.mapContainer}>

        <GoogleMapReact
          bootstrapURLKeys={{ key: Config.googleMapKey }}
          defaultCenter={this.state.center}
          defaultZoom={this.state.zoom}
          yesIWantToUseGoogleMapApiInternals
          onGoogleApiLoaded={({ map, maps }) => this.handleApiLoaded(map, maps)}>

          {items}

          {/*{*/}

            {/*this.props.predictions.map(function(ele){*/}
              {/*return (*/}
                {/*<MarkedArea*/}
                  {/*locationName={ele.location.name}*/}
                  {/*lat={ele.location.lat}*/}
                  {/*lng={ele.location.long}*/}
                  {/*size={15}*/}
                  {/*intensity={1}*/}
                {/*/>*/}
              {/*)*/}
            {/*})*/}
          {/*}*/}


          {/*<MarkedArea*/}
            {/*locationName={"Srinagar"}*/}
            {/*lat={34.0857}*/}
            {/*lng={74.8056}*/}
            {/*size={15}*/}
            {/*intensity={1}*/}
          {/*/>*/}

          {/*<MarkedArea*/}
            {/*locationName={"Bhubaneswar"}*/}
            {/*lat={20.2724}*/}
            {/*lng={85.8338}*/}
            {/*size={15}*/}
            {/*intensity={1}*/}
          {/*/>*/}

        </GoogleMapReact>

      </div>
    );
  }
}

const styles = {
  mapContainer: {
    position: 'absolute',
    top: '0vh',
    height: '100vh',
    width: '75vw'
  }
};

export default Map;
