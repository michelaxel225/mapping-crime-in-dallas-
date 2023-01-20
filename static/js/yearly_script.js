// Creating our initial map object:
// We set the longitude, latitude, and starting zoom level.
// This gets inserted into the div with an id of "map".
let myMap = L.map("map", {
    center: [32.799, -96.797],
    zoom: 11
  
  });
  
  // Adding a tile layer (the background map image) to our map:
  // We use the addTo() method to add objects to our map.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
  
  //------markercluster only--------------
  var markers = L.markerClusterGroup();
  
  // this add marker for every crime 
  for (i=0; i<year_data.length;i++) {
  let item = year_data[i]
  // console.log([item.lat, item.lon])
    markers.addLayer(L.marker([item.lat, item.lon], {
    draggable: false
  }).bindPopup(`<h3>Drug Arrest Found!<h3><h4>${item.sex}, ${item.age}</h4>Arrested for: ${item.drugtype}<br>Arrested at: ${item.arladdress}<br>Time: ${item.ararresttime}<br>`).openPopup()) 
  };
  
  myMap.addLayer(markers);
  
  //------------------------------------
  
  //heatmap----------------------
  var heatArray = [];
  
  for (let i = 0; i < year_data.length; i++) {
    let location = year_data[i];
      heatArray.push([parseFloat(location.lat).toFixed(4), parseFloat(location.lon).toFixed(4), 10]); //we rounded long and lat and gave weight 
  }
  
  console.log(heatArray)
  var heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 30
  }).addTo(myMap);
  
  
  //-------get our charts------------------
  
  let yearly_drugs = year_data.map(data => data.drugtype).filter(data => data != null)
  let drugs=['Marijuana', 'Cocaine', 'Meth','Heroin','Hydrocone','Ectasy','Oxycodone', 'GHB', 'Ketamine','Other <br>Prescription Drugs','Other <br>Non-Prescription Drugs']
  // create a counter for each drug group so it can be totaled
  let marijuana = 0;
  let meth = 0;
  let coke=0;
  let heroin=0;
  let otherPDrug=0;
  let otherNPdrug=0;
  let hydrocodone=0;
  let ectasy=0;
  let Oxycodone=0;
  let GHB=0;
  let Ketamine=0;
  //for loop through year_data.js get the drug name and put them in their categories
  for (let i=0; i<year_data.length; i++) {
    let item=year_data[i];
    
    if (item.drugtype == 'Cultivated Marijuana' || item.drugtype == 'Processed Marijuana' ){marijuana++} 
    else if (item.drugtype ==  'Methamphetamine'){meth++}
    else if (item.drugtype == 'Crack Cocaine' || item.drugtype == 'Powder Cocaine'){coke++}
    else if (item.drugtype == 'Heroin'){heroin++}
    else if (item.drugtype ==  'Other Prescription Drugs'){otherPDrug++}
    else if (item.drugtype ==  'Other Non-Prescription Drugs'){otherNPdrug++}
    else if (item.drugtype == 'Hydrocodone'){hydrocodone++}
    else if (item.drugtype == 'Ecstacy'){ectasy++}
    else if (item.drugtype == 'Oxycodone'){Oxycodone++}
    else if (item.drugtype == 'GHB'){GHB++}
    else if (item.drugtype == 'Ketamine'){Ketamine++}
  
    
  };
  //plots the # of arrests based on Drug
  let trace1 = {
    x: drugs,
    y: [marijuana,coke,meth,heroin,hydrocodone, ectasy, Oxycodone,GHB, Ketamine, otherPDrug,otherNPdrug],
    type: 'bar',
    marker:{color: ['rgb(84,176,17)','rgb(70,0,60)','rgb(166,166,40)','rgb(0,124,195)','rgb(0,0,195)','rgb(97,0,73)','rgb(0,124,0)','rgb(7,95,200)','rgb(142,124,195)','rgb(255,50,255)','rgb(229,137,20)']}
  };
  
  let data = [trace1];
  
  //a bunch of formatting for bar chart
  let layout = {
  title: {text:"Popular Drugs During Arrests",
          font:{size: 30}
        },
  paper_bgcolor: 'lightgrey',
  plot_bgcolor: 'rgba(245,246,249,1)',
  width: 1000,
  height: 600,
  font:{
    family: 'Roboto, monospace'
  },
  xaxis: {
    automargin: true,
    title: {
      text: 'Drug Name',
      font: {
        family: 'Roboto, monospace',
        size: 25
      }
    },
    tickfont: {
      size: 15,
      color: 'black'
    },
    anchor: 'free'
  }, 
  yaxis: {
    title: {
      text: 'Number of Arrests',
      font: {
        family: 'Roboto, monospace',
        size: 25
      }
    },
    tickfont: {
      size: 20,
      color: 'black'
    }
    
    
  },
  };
  
  Plotly.newPlot("chart1", data, layout);
  
  // get the number of male and females
  let num_males =0
  let num_females=0
  // for loops through your data to get number of male and females
  for (let i=0; i<year_data.length; i++) {
  let item=year_data[i];
  
  if (item.sex == "Male"){num_males++} 
  else{
    num_females++
  }
  };
  
  //pie plotly with num_male and num_females
  let pie_data = [{
  values: [num_males, num_females],  //used here
  labels: ['Male', 'Female'],
  type: 'pie',
  marker: {
    colors:['rgb(146,43,33)', 'rgb(40,116,166)']
  },
  textinfo: "label+percent",
  }];
  
  //a bunch of formatting for bar chart
  
  let pie_layout = {
  title:'The Percent of Arrest Men vs Women',
  font:{family: 'Roboto, monospace',size:20},
  paper_bgcolor: 'lightgrey',
  height: 500,
  width: 600,
  showlegend:false,
  margin: {"t": 100, "b": 10, "l": 10, "r": 10}
  
  };
  
  Plotly.newPlot('chart2', pie_data, pie_layout);
  
  
  
  