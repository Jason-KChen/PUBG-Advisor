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

export default function TimePhaseCard() {
    const classes = useStyles();
    
    return (
        // {/* <Card className={classes.root} variant="outlined"> */}
        <Card style={{ minWidth: 275,}}  variant="outlined">
            <CardContent>
              <Typography variant="h5" component="h2">
                PHASE #
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