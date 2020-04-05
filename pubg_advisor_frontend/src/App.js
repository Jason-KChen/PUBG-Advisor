import './App.css';
import React, {Component, useEffect} from 'react';
import { TabView } from './tabs/TabView';
import Leaflet from 'leaflet';
import {h337} from 'heatmap.js';
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';
import { Map, ImageOverlay, TileLayer, Marker, Popup} from "react-leaflet";
// import L from 'leaflet';

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




class MapComponent extends Component {
    

    constructor(props) {
        super(props)
        var fileName = this.getMapFileName(mapNames[0])
        this.state = {
            currentMap: mapNames[0],
            currentMapFile: this.getMapFileName(mapNames[0])
        };
        // this.handleSelect = this.handleSelect.bind(this);
    }

    getMapFileName(mapName) {
        var fileName =null;
        if (mapName == "Camp Jackal") {
            fileName = "Camp_Jackal";
        } else {
            fileName = mapName;
        }
        return fileName;
    }

    handleSelect = (selectedMap) =>{
        console.log(selectedMap);
        var fileName = this.getMapFileName(selectedMap);

        this.setState(
            {currentMap: selectedMap,
            currentMapFile: fileName
            }
        );
    }

    componentDidMount() {

        // var heatmapInstance = h337.create({
        //   // only container is required, the rest will be defaults
        //   container: document.querySelector('.mapContainer')
        // });
        
        
        // if you have a set of datapoints always use setData instead of addData
        // for data initialization
        // heatmapInstance.setData(data);
        
        // heatmapLayer.setData(data);
        
    }

    render() {
        var points = [];
        var max = 0;
        var width = 840;
        var height = 400;
        var len = 200;

        while (len--) {
          var val = Math.floor(Math.random()*100);
          max = Math.max(max, val);
          var point = [
             Math.floor(Math.random()*width),
             Math.floor(Math.random()*height)
              ];
          points.push(point);
        }
        // heatmap data format
        var data = {
          data: points
        };
        console.log(points);
        const center = [0,0];
        var b = 300;

        function ListItem(args) {
            return <Dropdown.Item onSelect={args.handleSelect} eventKey={args.name}>{args.name}</Dropdown.Item>
        }
        // <img src={"maps/" + this.state.currentMapFile + ".png"}/>
        return(
            <div>
                <DropdownButton id="dropdown-basic-button" title={this.state.currentMap} >
                    {mapNames.map((value, index) => {
                        return <ListItem key={index} name={value} handleSelect={this.handleSelect}/>

                    })}
                </DropdownButton>
                <Map center={[b/2,b/2]} zoom={4} ref={(ref) => { this.map = ref; }} setMaxBounds={[[0,0], [b,b]] } crs={Leaflet.CRS.Simple}>
                    <HeatmapLayer
                        fitBoundsOnLoad
                        fitBoundsOnUpdate
                        points={points}
                        longitudeExtractor={m => m[1]}
                        latitudeExtractor={m => m[0]}
                        intensityExtractor={m => parseFloat(m[2])} />
                    <ImageOverlay url={"maps/" + this.state.currentMapFile+ ".png"} bounds={[[0,0], [b,b]]}/>
                </Map>}
            </div>
        );
    
    }
    
}

class App extends Component
   {
  

  render() {

    return (
        <MapComponent/>   
    );
  }
}
export default App;
  