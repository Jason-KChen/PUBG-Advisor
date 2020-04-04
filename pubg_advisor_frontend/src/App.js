import './App.css';
import React, {Component, useEffect} from 'react';
import { TabView } from './tabs/TabView';
import h337   from 'heatmap.js'
import DropdownButton from 'react-bootstrap/DropdownButton'
import Dropdown from 'react-bootstrap/Dropdown'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';

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


const mapNames = ["Camp Jackal", "Erangel", "Karakin", "Miramar", "Sanhok", "Vikendi"];


class MapContainer extends Component {
  

  constructor(props) {
    super(props)
    this.state = {
      currentMap: mapNames[0],
    };
  }
  render() {
    const buttonRef = React.createRef();
    

    function handleSelect(e) {
      console.log(e);
      this.setState(
        (state, e) => {
          return {currentMap: e};
        }
      );
    }

    function ListItem(args) {
      return <Dropdown.Item onSelect={() => handleSelect} eventKey={args.name}>{args.name}</Dropdown.Item>
    }

    return(
      <div>
        <DropdownButton id="dropdown-basic-button" title={this.state.currentMap} ref = {buttonRef}>
            {mapNames.map((value, index) => {
              return <ListItem key={index} name={value} />
            })}
        </DropdownButton>
      </div>
      );
  }

}


class App extends Component{
  

  componentDidMount() {
    console.log('I am mounted!');
    var heatmapInstance = h337.create({
      // only container is required, the rest will be defaults
      container: document.querySelector('.mapContainer')
    });
    // now generate some random data
    var points = [];
    var max = 0;
    var width = 840;
    var height = 400;
    var len = 200;

    while (len--) {
      var val = Math.floor(Math.random()*100);
      max = Math.max(max, val);
      var point = {
        x: Math.floor(Math.random()*width),
        y: Math.floor(Math.random()*height),
        value: val
      };
      points.push(point);
    }
    // heatmap data format
    var data = {
      max: max,
      data: [{x: 10, y:33, value: 200},{x: 10, y:30, value: 2000},{x: 10, y:40, value: 2000},{x: 10, y:50, value: 2000}]
    };
    // if you have a set of datapoints always use setData instead of addData
    // for data initialization
    heatmapInstance.setData(data);
  }
  
  render() {
     return (
    <div className="mapContainer">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
  }
}
export default App;
  