import React from 'react';
import { Typography } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';
import TimePhaseCard from './TimePhaseCard';
import SimpleBar from 'simplebar-react';
import 'simplebar/dist/simplebar.min.css';

import './RankingPanel.css';
import { TimePhaseCardParam } from './TimePhaseCardParam';




class RankingPanel extends React.Component {
  state = {
    first: ["A", "B", "C"],
    second: [],
    third: []
  }

  async componentDidMount() {
    try {
      let res = await fetch("http://ec2-18-233-8-23.compute-1.amazonaws.com:12315/weapon_ranking", {
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      })
      const data = await res.json()

      console.log(data)
    } catch (err) {
      console.log(err)
    }
  }

  render() {
    // const classes = useStyles();
    return (
      <div className="col panel-layout">
        <Typography>
          Ranking Table here TODO
        </Typography>
        <SimpleBar style={{ maxHeight: 490 }}>
        <ul id="parent">
          <li>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "1"/>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "3" />
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "2"/>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "4"/>
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "5"/>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "7"/>
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "6"/>
          <TimePhaseCardParam weaponsForThisStage={this.state.first} num = "8"/>
          </li>
        </ul>
        </SimpleBar>
      </div>
    );
  }
}

export { RankingPanel };
