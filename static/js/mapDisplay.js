

function initMap() {

    let latitudeValue = parseFloat(document.getElementById("latitude").textContent);
    let longitudeValue = parseFloat(document.getElementById("longitude").textContent);
    let centerLat = parseFloat(document.getElementById("centreLat").textContent);
    let centreLon = parseFloat(document.getElementById("centreLon").textContent);
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: centerLat, lng: centreLon },
    mapTypeId: "terrain",
  });


    const obfsCircle = new google.maps.Circle({
      strokeColor: "#FF0000",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0.35,
      map,
      center: {lat :latitudeValue, lng: longitudeValue},
      radius: 1000,
    });

}
window.initMap = initMap;