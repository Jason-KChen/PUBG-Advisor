import React from 'react';
import { Typography } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';

import WeaponExpansion from './WeaponExpansion'

const useStyles = makeStyles({
    root: {
      minWidth: 275,
    },
    title: {
      fontSize: 14,
    },
    pos: {
      marginBottom: 12,
      // display: inline-block,
    },
  });

  class TimePhaseCardParam extends React.Component{
    constructor(props){
     super(props);
        this.state={
           cardNum:"",
         };
      }
    componentDidMount(){
        this.setState({
            cardNum: this.props.num,
        });
    }
  // componentWillRecieveProps(nextProps,nextState){
  //   this.setState({
  //    cardNum:nextProps["num"],
  //    });

  //   }
  //   shouldComponentUpdate(nextProps,nextState){
  //      // your condition if you want to re-render every time on props change
  //    return true;
  //   }
    render() {
    return (
        // {/* <Card className={classes.root} variant="outlined"> */}
        <Card num={this.state.cardNum} style={{ minWidth: 275,}}  variant="outlined">
            <CardContent>
              <Typography variant="h5" component="h2">
                PHASE # {this.state.cardNum}
              </Typography>
              {/* <Typography className={classes.pos} color="textSecondary"> */}
              <Typography style={{ marginBottom: 12,}} color="textSecondary">
                Description of Phase
              </Typography>
            </CardContent>
            <CardActions>
              <WeaponExpansion/>
            </CardActions>
        </Card>
    );
    }
}    
export { TimePhaseCardParam };
