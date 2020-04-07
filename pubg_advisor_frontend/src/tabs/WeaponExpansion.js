import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MuiExpansionPanel from '@material-ui/core/ExpansionPanel';
import MuiExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import MuiExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import Item_Weapon_Mini14_C from './Item_Weapon_Mini14_C.png';
import Item_Attach_Weapon_Muzzle_Suppressor_Small_C from './Item_Attach_Weapon_Muzzle_Suppressor_Small_C.png'
import Item_Attach_Weapon_Upper_CQBSS_C from './Item_Attach_Weapon_Upper_CQBSS_C.png'

import './WeaponExpansion.css';

const ExpansionPanel = withStyles({
  root: {
    border: '1px solid rgba(0, 0, 0, .125)',
    maxWidth: 357,
    boxShadow: 'none',
    '&:not(:last-child)': {
      borderBottom: 0,
    },
    '&:before': {
      display: 'none',
    },
    '&$expanded': {
      margin: 'auto',
    },
  },
  expanded: {},
})(MuiExpansionPanel);

const ExpansionPanelSummary = withStyles({
  root: {
    backgroundColor: 'rgba(0, 0, 0, .03)',
    borderBottom: '1px solid rgba(0, 0, 0, .125)',
    marginBottom: -1,
    minWidth: 310,
    minHeight: 56,
    '&$expanded': {
      minHeight: 56,
    },
  },
  content: {
    '&$expanded': {
      margin: '12px 0',
    },

  },
  expanded: {},
})(MuiExpansionPanelSummary);

const ExpansionPanelDetails = withStyles((theme) => ({
  root: {
    height: 120,
    // padding: theme.spacing(2),
  },
}))(MuiExpansionPanelDetails);

export default function WeaponExpansion() {
  const [expanded, setExpanded] = React.useState('panel1');

  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  return (
    <div>
      <ExpansionPanel square expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
        <ExpansionPanelSummary aria-controls="panel1d-content" id="panel1d-header">
          <Typography>Top #1: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <img style={{ 
              height: 150, width:300, alignItems:'center', transform:'rotate(-23deg)'}} 
              src={Item_Weapon_Mini14_C} alt="Item_Weapon_Mini14_C" />
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li2>
          <Typography>
            Muzzle:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={Item_Attach_Weapon_Muzzle_Suppressor_Small_C} alt="Item_Attach_Weapon_Muzzle_Suppressor_Small_C" />
          </Typography>
            Name of Muzzle
          </li2>
          <li2>
          <Typography>
            Scope:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={Item_Attach_Weapon_Upper_CQBSS_C} alt="Item_Attach_Weapon_Upper_CQBSS_C" />
          </Typography>
          Name of Scope
          </li2>
        </ul>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
        <ExpansionPanelSummary aria-controls="panel2d-content" id="panel2d-header">
          <Typography>Top #2: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
        <ExpansionPanelSummary aria-controls="panel3d-content" id="panel3d-header">
          <Typography>Top #3: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

        </ExpansionPanelDetails>
      </ExpansionPanel>
    </div>
  );
}