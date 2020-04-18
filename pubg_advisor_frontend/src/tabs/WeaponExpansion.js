import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MuiExpansionPanel from '@material-ui/core/ExpansionPanel';
import MuiExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import MuiExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';

import WeapHK416_C from './GunsAndAttachments/Item_WeapHK416_C.png'
import WeapAK47_C from './GunsAndAttachments/Item_WeapAK47_C.png'
import WeapFNFal_C from './GunsAndAttachments/Item_WeapFNFal_C.png'
import WeapSCARL_C from './GunsAndAttachments/Item_WeapSCAR-L_C.png'
import WeapSKS_C from './GunsAndAttachments/Item_WeapSKS_C.png'
import Item_Weapon_Mini14_C from './GunsAndAttachments/Item_Weapon_Mini14_C.png';

import Item_Attach_Weapon_Muzzle_Suppressor_Small_C from './GunsAndAttachments/Item_Attach_Weapon_Muzzle_Suppressor_Small_C.png'
import Item_Attach_Weapon_Muzzle_Compensator_Large_C from './GunsAndAttachments/Item_Attach_Weapon_Muzzle_Compensator_Large_C.png'
import Item_Attach_Weapon_Muzzle_Suppressor_Large_C from './GunsAndAttachments/Item_Attach_Weapon_Muzzle_Suppressor_Large_C.png'
import Item_Attach_Weapon_Muzzle_FlashHider_Large_C from './GunsAndAttachments/Item_Attach_Weapon_Muzzle_FlashHider_Large_C.png'
import Item_Attach_Weapon_Muzzle_Suppressor_SniperRifle_C from './GunsAndAttachments/Item_Attach_Weapon_Muzzle_Suppressor_SniperRifle_C.png'

import Item_Attach_Weapon_Upper_DotSight_01_C from './GunsAndAttachments/Item_Attach_Weapon_Upper_DotSight_01_C.png'
import Item_Attach_Weapon_Upper_CQBSS_C from './GunsAndAttachments/Item_Attach_Weapon_Upper_CQBSS_C.png';
import Item_Attach_Weapon_Upper_Scope6x_C from './GunsAndAttachments/Item_Attach_Weapon_Upper_Scope6x_C.png'

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

export default function WeaponExpansion(props) {
  const [expanded, setExpanded] = React.useState('panel1');

  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };
  console.log(props.weapons[0])
  console.log(`./GunsAndAttachments/${props.weapons[0][2]}.png`)
  if (props.weapons[0].length == 0) {
    return(
      <div>
      <ExpansionPanel square expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
        <ExpansionPanelSummary aria-controls="panel1d-content" id="panel1d-header">
          <Typography>Top #1: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
              
          </Typography>
            {props.weapons[0][1]}
          </li>
          <li>
          <Typography>
            Scope:
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
        <ExpansionPanelSummary aria-controls="panel2d-content" id="panel2d-header">
          <Typography>Top #2: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
          </Typography>
            {props.weapons[1][1]}
          </li>
          <li>
          <Typography>
            Scope:
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
        <ExpansionPanelSummary aria-controls="panel3d-content" id="panel3d-header">
          <Typography>Top #3: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
          </Typography>
            {props.weapons[2][1]}
          </li>
          <li>
          <Typography>
            Scope:
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
    </div>
    )
  } else {
  return (
    <div>
      <ExpansionPanel square expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
        <ExpansionPanelSummary aria-controls="panel1d-content" id="panel1d-header">
          <Typography>Top #1: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <img style={{ 
              height: 150, width:300, alignItems:'center', transform:'rotate(-23deg)'}} 
              src={require(`./GunsAndAttachments/Item_${props.weapons[0][3]}.png`)} alt="Item_Weapon_Mini14_C" />
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
            {/* switch (props.weapons) {
                case 'Item_Attach_Weapon_Muzzle_Suppressor_Small_C':
                  var={Item_Attach_Weapon_Muzzle_Suppressor_Small_C}
                  break;
              } */}
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[0][1]}.png`)} alt= {props.weapons}/>

              {/* src={props.weapons} alt= {props.weapons.toString()}/> */}
              
          </Typography>
            {props.weapons[0][1]}
          </li>
          <li>
          <Typography>
            Scope:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[0][2]}.png`)} alt="Item_Attach_Weapon_Upper_CQBSS_C" />
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
        <ExpansionPanelSummary aria-controls="panel2d-content" id="panel2d-header">
          <Typography>Top #2: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

        <img style={{ 
              height: 150, width:300, alignItems:'center', transform:'rotate(-23deg)'}} 
              src={require(`./GunsAndAttachments/Item_${props.weapons[1][3]}.png`)} alt="Item_Weapon_Mini14_C" />
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[1][1]}.png`)} alt="Item_Weapon_Mini14_C" />
          </Typography>
            {props.weapons[1][1]}
          </li>
          <li>
          <Typography>
            Scope:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[1][2]}.png`)} alt="Item_Attach_Weapon_Upper_CQBSS_C" />
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
      <ExpansionPanel square expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
        <ExpansionPanelSummary aria-controls="panel3d-content" id="panel3d-header">
          <Typography>Top #3: NAME OF WEAPON</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

        <img style={{ 
              height: 150, width:300, alignItems:'center', transform:'rotate(-23deg)'}} 
              src={require(`./GunsAndAttachments/Item_${props.weapons[2][3]}.png`)} alt="Item_Weapon_Mini14_C" />
        </ExpansionPanelDetails>
        <ul id="parent2">
          <li>
          <Typography>
            Muzzle:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[2][1]}.png`)} alt="Item_Weapon_Mini14_C" />
          </Typography>
            {props.weapons[2][1]}
          </li>
          <li>
          <Typography>
            Scope:
            <img style={{ 
              height: 50, width:60, alignItems:'center', transform:'rotate(40deg)'}} 
              src={require(`./GunsAndAttachments/${props.weapons[2][2]}.png`)} alt="Item_Attach_Weapon_Upper_CQBSS_C" />
          </Typography>
          {props.weapons[0][2]}
          </li>
        </ul>
      </ExpansionPanel>
    </div>
  );
            }
}
