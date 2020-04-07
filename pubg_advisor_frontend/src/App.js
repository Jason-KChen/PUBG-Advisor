import './App.css';
import React from 'react';
import { TabView } from './tabs/TabView';

function getStyles() {
  return {
    // Position the Panel in the middle of the screen
    backgroundStyle: {
      justifyContent: "center",
      alignItems: "center"
    },
    // Size of the Panel relative to the whole screen
    tabViewWrapper: {
      width: "70%",
      height: "70%"
    }
  }
}

function App() {
  let styles = getStyles();

  return (
    <div className="background col" style={styles.backgroundStyle}>
      <div style={styles.tabViewWrapper}>
        <TabView />
      </div>
    </div>
  );
}

export default App;
