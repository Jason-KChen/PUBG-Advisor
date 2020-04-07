import React from 'react';
import { Typography } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';
import TimePhaseCard from './TimePhaseCard';
import SimpleBar from 'simplebar-react';
import 'simplebar/dist/simplebar.min.css';

import './RankingPanel.css';
import { TimePhaseCardParam } from './TimePhaseCardParam';




class RankingPanel extends React.Component {

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
          <TimePhaseCardParam num = "1"/>
          <TimePhaseCardParam num = "3" />
          </li>
          <li>
          <TimePhaseCardParam num = "2"/>
          <TimePhaseCardParam num = "4"/>
          </li>
          <li>
          <TimePhaseCardParam num = "5"/>
          <TimePhaseCardParam num = "7"/>
          </li>
          <li>
          <TimePhaseCardParam num = "6"/>
          <TimePhaseCardParam num = "8"/>
          </li>
        </ul>
        </SimpleBar>
      </div>
    );
  }
}

export { RankingPanel };
