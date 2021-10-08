// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
  console.log(data.features)
});

    // Create  layer groups for circles
    var circleLayer = L.layerGroup(circleArray);

    // Create an overlayMaps object to contain the "State Population" and "City Population" layers
    var overlayMaps = {
        "Marker Clusters": earthquakeMarkers,
        // "Earthquakes": geoLayer,
        "Circles": circleLayer
};

function createFeatures(earthquakeData) {

  // Define a function we want to run once for each feature in the features array
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>${feature.properties.place}
                     Mag: ${feature.properties.mag} </h3><hr><p>${new Date(feature.properties.time)}</p> `);
  }

//   function onEachFeature(feature, layer) {
//     layer.bindPopup("<h4>Location: " + feature.properties.place + 
//     "</h4><hr><p>Date & Time: " + new Date(feature.properties.time) + 
//     "</p><hr><p>Magnitude: " + feature.properties.mag + "</p>");
//   }

  // Define function to create the circle radius based on the magnitude
  function radiusSize(magnitude) {
    return magnitude * 50000;
  }

  // Define function to set the circle color based on the magnitude
  function circleColor(magnitude) {
    if (magnitude > 5) {
      return "mediumslateblue"
    }
    else if (magnitude > 4) {
      return "firebrick"
    }
    else if (magnitude > 3) {
    return "coral"
    }
    else if (magnitude > 2) {
      return "gold"
    }
    else if (magnitude > 1) {
      return "yellowgreen"
    }
    else {
      return "darkturquoise"
    }
  }

  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    pointToLayer: function(earthquakeData, latlng) {
      return L.circle(latlng, {
        radius: radiusSize(earthquakeData.properties.mag),
        color: circleColor(earthquakeData.properties.mag),
        fillOpacity: 0
      });
    },
    onEachFeature: onEachFeature
  });

  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

    // Define satellitemap, darkmap, and lightmap layers
    var satellitemap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/satellite-v9',
        accessToken: API_KEY
    });

    var darkmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/dark-v10',
        accessToken: API_KEY
    });
  
    var lightmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/light-v10',
        accessToken: API_KEY
    });
  
    // Create the faultline layer
    var tectplates = new L.LayerGroup();
    
    // Define a baseMaps object to hold our base layers
    var baseMaps = { 
      "Light Map": lightmap,
      "Dark Map": darkmap,
      "Satellite Map": satellitemap     
    };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    "Earthquakes": earthquakes,
    "Tectonic Plates": tectplates
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 4,
    layers: [lightmap, tectplates]
  });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  // Query to retrieve the tectonic plates data
  var tectplatesquery = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json";
  
  // Create the tectplates and add them to the tectplates layer
  d3.json(tectplatesquery, function(data) {
    L.geoJSON(data, {
      style: function() {
        return {color: "orange", fillOpacity: 0}
      }
    }).addTo(tectplates)
  })

//   color function to be used when creating the legend
function chooseColor(magnitude) { 
    if (magnitude > 5) {
      return "mediumslateblue"
    }
    else if (magnitude > 4) {
      return "firebrick"
    }
    else if (magnitude > 3) {
    return "coral"
    }
    else if (magnitude > 2) {
      return "gold"
    }
    else if (magnitude > 1) {
      return "yellowgreen"
    }
    else {
      return "darkturquoise"
    }
  }

  // Add legend to the map
  var legend = L.control({position: 'bottomright'});
  
  legend.onAdd = function () {
  
    var div = L.DomUtil.create('div', 'info legend'),
    mags = [0, 1, 2, 3, 4, 5];
        // labels = [];
    div.innerHTML += "<h3>Magnitude</h3>"
      // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < mags.length; i++) {
        div.innerHTML +=
            '<i style="background:' + chooseColor(mags[i] + 1) + '"></i> ' +
            mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+');
    }
  
      return div;
  };
  
  legend.addTo(myMap);
}