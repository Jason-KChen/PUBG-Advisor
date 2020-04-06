import './App.css';
import React, {Component, useEffect} from 'react';
import { TabView } from './tabs/TabView';
import Leaflet from 'leaflet';
import {h337} from 'heatmap.js';
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';
import { Map, ImageOverlay, TileLayer, Marker, Popup, CircleMarker} from "react-leaflet";
import L from 'leaflet';

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


class SearchCircle extends Component {
    constructor(props) {
        super(props);
    }
}

class MapComponent extends Component {
    

    constructor(props) {
        super(props)
        var fileName = this.getMapFileName(mapNames[0])
        this.state = {
            currentMap: mapNames[0],
            currentMapFile: this.getMapFileName(mapNames[0]),
            selectedPoint: null,
            selectedRadius: null
        };
        // this.handleSelect = this.handleSelect.bind(this);
        this.updateCircle = this.updateCircle.bind(this);
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

    handleSelect = (selectedMap) => {
        console.log(selectedMap);
        var fileName = this.getMapFileName(selectedMap);

        this.setState(
            {currentMap: selectedMap,
            currentMapFile: fileName,
            selectedPoint: this.state.selectedPoint,
            selectedRadius: this.state.selectedRadius
            }
        );
    }


    userMapClick = (newPoint) => {
        this.setState(
            {currentMap: this.state.currentMap,
            currentMapFile: this.state.currentMapFile,
            selectedPoint: newPoint.latlng,
            selectedRadius: 20
            }
        );
    }
    
    updateCircle(newRadius) {
        console.log(newRadius);
        this.setState(
            {currentMap: this.state.currentMap,
            currentMapFile: this.state.currentMapFile,
            selectedPoint: this.state.selectedPoint,
            selectedRadius: newRadius.target.value
            }
        );
    }

    render() {
        
        const center = [0,0];
        var b = 300;

        function ListItem(args) {
            return <Dropdown.Item onSelect={args.handleSelect} eventKey={args.name}>{args.name}</Dropdown.Item>
        }

        var points = [];
        
     
        return(

            <div>
                
                <DropdownButton id="dropdown-basic-button" title={this.state.currentMap} >
                    {mapNames.map((value, index) => {
                        return <ListItem key={index} name={value} handleSelect={this.handleSelect}/>

                    })}
                </DropdownButton>
                <Map center={this.state.selectedPoint ? this.state.selectedPoint :[b/2,b/2]} zoom={2} id="physicalMap" ref={(ref) => { this.map = ref; }} setMaxBounds={[[0,0], [b,b]] } crs={Leaflet.CRS.Simple} onClick={this.userMapClick}>
                    <HeatmapLayer
                        fitBoundsOnLoad
                        fitBoundsOnUpdate
                        points = {
                            points
                        }
                        longitudeExtractor={m => m[1]}
                        latitudeExtractor={m => m[0]}
                        intensityExtractor={m => parseFloat(m[2])} />
                    <ImageOverlay url={"maps/" + this.state.currentMapFile+ ".png"} bounds={[[0,0], [b,b]]}/>
                    { this.state.selectedPoint !== null &&
                        <Marker position={this.state.selectedPoint}>
                            <Popup>
                                <form onSubmit={this.handleSubmit}>
                                    <label>
                                      Search Radius
                                        <input value={this.state.selectedRadius} onChange={this.updateCircle} />
                                    </label>
                                    <input type="submit" value="Submit" />
                                </form>
                            </Popup>
                        </Marker> 
                    } 
                    {
                        this.state.selectedPoint !== null &&
                        <CircleMarker center={this.state.selectedPoint} color="red" radius={this.state.selectedRadius}>
                            <Popup>Popup in CircleMarker</Popup>
                        </CircleMarker>
                    }
                </Map>}
            </div>
        );
    
    }
    
}

class App extends Component {
  
    render() {
        return (
            <MapComponent/>   
        );
    }
}
export default App;
