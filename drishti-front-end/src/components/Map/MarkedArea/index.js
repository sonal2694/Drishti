import React, { Component } from 'react';

class MarkedArea extends Component {

  constructor(props) {
    super(props);

    this.state = {
      intensity: props.intensity,
      size: props.size,
      markDynamicStyle: {
        width: props.size,
        height: props.size,
        opacity: props.intensity,
        backgroundColor: props.color,
        borderRadius: props.size,
        border: '4px solid #193341',
      },
      textLabelStyle: {
        backgroundColor: '#193341',
        padding: '4px',
        color: '#fff',
        fontWeight: '500',
        margin: '20px'
      }
    };

    // this.markClicked().bind(this);

  }

  markClicked(e) {
    alert('clicked')
  }

  render() {

    return (
      <div>
        <div style={this.state.markDynamicStyle} onClick={this.markClicked}></div>
        <span style={this.state.textLabelStyle}>{this.props.locationName}</span>
      </div>

    );
  }

};



export default MarkedArea;