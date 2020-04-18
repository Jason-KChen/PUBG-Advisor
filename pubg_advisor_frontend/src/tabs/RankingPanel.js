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
    firstOne: [],
    firstTwo: [],
    firstThree: [],
    firstFour: [],
    firstFive: [],
    firstSix: [],
    firstSeven: [],
    firstEight: [],
    secondOne: [],
    secondTwo: [],
    secondThree: [],
    secondFour: [],
    secondFive: [],
    secondSix: [],
    secondSeven: [],
    secondEight: [],
    thirdOne: [],
    thirdTwo: [],
    thirdThree: [],
    thirdFour: [],
    thirdFive: [],
    thirdSix: [],
    thirdSeven: [],
    thirdOnEight: [],
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
      this.setState({
        firstOne: Object.values(data.first[0]),
        firstTwo: Object.values(data.first[1]),
        firstThree: Object.values(data.first[2]),
        firstFour: Object.values(data.first[3]),
        firstFive: Object.values(data.first[4]),
        firstSix: Object.values(data.first[5]),
        firstSeven: Object.values(data.first[6]),
        firstEight: Object.values(data.first[7]),
        secondOne: Object.values(data.second[0]),
        secondTwo: Object.values(data.second[1]),
        secondThree: Object.values(data.second[2]),
        secondFour: Object.values(data.second[3]),
        secondFive: Object.values(data.second[4]),
        secondSix: Object.values(data.second[5]),
        secondSeven: Object.values(data.second[6]),
        secondEight: Object.values(data.second[7]),
        thirdOne: Object.values(data.third[0]),
        thirdTwo: Object.values(data.third[1]),
        thirdThree: Object.values(data.third[2]),
        thirdFour: Object.values(data.third[3]),
        thirdFive: Object.values(data.third[4]),
        thirdSix: Object.values(data.third[5]),
        thirdSeven: Object.values(data.third[6]),
        thirdOnEight: Object.values(data.third[7]),
      })
      console.log(data)
      console.log(this.state.second)
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
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstOne, this.state.secondOne, this.state.thirdOne]} num = "1"/>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstThree, this.state.secondThree, this.state.thirdThree]} num = "3" />
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstTwo, this.state.secondTwo, this.state.thirdTwo]} num = "2"/>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstFour, this.state.secondFour, this.state.thirdFour]} num = "4"/>
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstFive, this.state.secondFive, this.state.thirdFive]} num = "5"/>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstSeven, this.state.secondSeven, this.state.thirdSeven]} num = "7"/>
          </li>
          <li>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstSix, this.state.secondSix, this.state.thirdSix]} num = "6"/>
          <TimePhaseCardParam weaponsForThisStage={[this.state.firstEight, this.state.secondEight, this.state.thirdOnEight]} num = "8"/>
          </li>
        </ul>
        </SimpleBar>
      </div>
    );
  }
}

export { RankingPanel };
