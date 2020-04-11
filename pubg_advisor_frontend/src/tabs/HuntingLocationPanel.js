import React, { Component } from 'react';
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { Map, ImageOverlay, Marker, Popup, CircleMarker } from "react-leaflet";
import  HashMap  from 'hashmap';
import { NativeSelect } from '@material-ui/core';
import L from 'leaflet';
import './HuntingLocationPanel.css';
import { MAPNAMES, MAPDIMENSIONS } from './tabsConstants.js';

class MapComponent extends Component {

  constructor(props) {
    super(props);
    var displayName = MAPNAMES[0][0];
    var fileName = this.getMapFileName(displayName);
    var apiNameMap = new HashMap(MAPNAMES);
    var mapDimensions = new HashMap(MAPDIMENSIONS);
    var initialMapDimension = mapDimensions.get(displayName);

    this.state = {
      currentMap: displayName,
      currentMapFile: fileName,
      currentMapDimension: initialMapDimension,
      selectedPoint: null,
      selectedRadius: null,
      apiNames: apiNameMap,
      mapDimensions: mapDimensions
    };
    this.updateCircle = this.updateCircle.bind(this);

  }

  getMapFileName(mapName) {
    var fileName = null;
    if (mapName === "Camp Jackal") {
      fileName = "Camp_Jackal";
    } else if (mapName === "Erangel (Remastered)") {
      fileName = "Erangel_Remastered";
    }else {
      fileName = mapName;
    }
    return fileName;
  }

  handleSelect = (event) => {
    var selectedMap = event.target.value;
    var fileName = this.getMapFileName(selectedMap);
    var nextMapDim = this.state.mapDimensions.get(selectedMap);
    this.setState({
      currentMap: selectedMap,
      currentMapFile: fileName,
      currentMapDimension: nextMapDim
    }, () => {
      console.log(this.state);
    });
  }


  userMapClick = (newPoint) => {
    this.setState({
      selectedPoint: newPoint.latlng,
      selectedRadius: 20,
    });
  }

  updateCircle(newRadius) {
    console.log(newRadius);
    this.setState({
      selectedRadius: newRadius.target.value,
    });
  }

  findKills = (clickEvent) => {
    clickEvent.preventDefault();
    console.log("Finding kills");
    console.log(this.state.selectedPoint);
    var mapAPIname = this.state.apiNames.get(this.state.currentMap);
    var x = this.state.selectedPoint.lng;
    var y = this.state.selectedPoint.lat;
    var radius = this.state.selectedRadius;
    fetch(`http://ec2-18-233-8-23.compute-1.amazonaws.com:12315/kill?map_name=${mapAPIname}&x=${x}&y=${y}&radius=${radius}`)
    .then((response) => {
      console.log(response);
    });
  }


  render() {
    function ListItem(args) {
      return <option value = {args.name} > {args.name} </option>
    }

    var points = [

    ];

    return (
      <div>
        <NativeSelect id="select" value={ this.state.currentMap} onChange={this.handleSelect} multiple={true}> 
          {
            MAPNAMES.map((value, index) => { 
              return <ListItem key={ index } name={ value[0] } /> 
            }) 
          }
        </NativeSelect>
        <Map center={ this.state.selectedPoint ? this.state.selectedPoint : [this.state.currentMapDimension / 2, this.state.currentMapDimension / 2] } 
        zoom={ 1 } id="physicalMap" ref={ (ref)=> { this.map = ref; } } 
        setMaxBounds = { [ [0, 0], [this.state.currentMapDimension, this.state.currentMapDimension] ] } 
        crs = { 
          L.extend({}, L.CRS.Simple, {
            projection: L.Projection.LonLat,
            transformation: new L.Transformation(.003, 0, .003, 0),
            scale: function(zoom) {
              return Math.pow(2, zoom);
            },

            zoom: function(scale) {
              return Math.log(scale) / Math.LN2;
            },

            distance: function(latlng1, latlng2) {
              var dx = latlng2.lng - latlng1.lng,
                dy = latlng2.lat - latlng1.lat;

              return Math.sqrt(dx * dx + dy * dy);
            },
            infinite: true
          })
        } 
        onClick = { this.userMapClick } >
          <HeatmapLayer fitBoundsOnLoad fitBoundsOnUpdate points={ points } longitudeExtractor={ m=> m[1] } 
          latitudeExtractor = { m => m[0] } intensityExtractor = { m => parseFloat(m[2]) } />
            <ImageOverlay url={ "maps/" + this.state.currentMapFile + ".png" } 
            bounds={ [ [0, 0], [this.state.currentMapDimension, this.state.currentMapDimension] ] } /> 
            { 
              this.state.selectedPoint !== null &&
              <Marker position={ this.state.selectedPoint }>
                <Popup>
                  <form onSubmit={ this.handleSubmit }>
                    <label>
                      Search Radius
                      <input value={ this.state.selectedRadius } onChange={ this.updateCircle } />
                    </label>
                    <input type="submit" value="Find Kills" onClick={this.findKills}/>
                  </form>
                </Popup>
              </Marker>
            } 
            { 
              this.state.selectedPoint !== null &&
              <CircleMarker center={ this.state.selectedPoint } color="red" radius={ this.state.selectedRadius }>
                <Popup> 
                  Popup in CircleMarker
                </Popup>
              </CircleMarker>
            }
        </Map>
      </div>
    );

  }

}


class HuntingLocationPanel extends Component {
  render() {
    return ( 
      <div className = "col panel-layout" >
        <MapComponent/>
      </div>
    );
  }
}

export {
  HuntingLocationPanel
};
