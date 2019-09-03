import React, { Component, StyleSheet } from 'react';
import './style.css';

const classNames = require('classnames');


class TestDateTile extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isHovered: false
    };

  }

  setTileHovered(flag) {
    console.log('here');
    let state = this.state;
    state.isHovered = flag;
    this.setState(state);
  }


  render() {
    return (
      <div
        className={classNames('tile', {isHovered: this.state.isHovered}, {isNotHovered: this.state.isNotHovered})}
        onMouseEnter={() => this.setTileHovered(true)}
        onMouseLeave={() => this.setTileHovered(false)}>

        test
      </div>
    );
  }
}


export default TestDateTile;
