import React from 'react';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

import { RankingPanel } from './RankingPanel';
import { HuntingLocationPanel } from './HuntingLocationPanel';


function getStyles() {
  return {
    panelBackground: {
      opacity: 0.85,
      background: 'white',
      borderRadius: '15px',
      height: '100%',
      width: '100%'
    },
    tabHeader: {
      height: '5%',
      borderTopRightRadius: '15px',
      borderTopLeftRadius: '15px'
    }
  };
}

class TabView extends React.Component {
  state = {
    panelIdx: 0,
  };

  handleChange = (_, panelIdx) => {
    this.setState({ panelIdx });
  };

  render() {
    const { panelIdx } = this.state;
    const styles = getStyles();

    return (
      <div
        className="col"
        id="ContentPaper"
        style={styles.panelBackground}
      >
        <Tabs
          className="hide-scroll-bar"
          value={panelIdx}
          onChange={this.handleChange}
          indicatorColor="primary"
          textColor="inherit"
          variant="fullWidth"
          style={styles.tabHeader}
        >
          <Tab label="Weapon Ranking" />
          <Tab label="Popular Hunting Spots" />
        </Tabs>
        {panelIdx === 0 && <RankingPanel />}
        {panelIdx === 1 && <HuntingLocationPanel />}
      </div>
    );
  }
}

export { TabView }
