$(document).ready(setUp);

function setUp() {
  $('.showInMap').click(geocode);
}

function geocode() {
  $.get(
     'https://maps.googleapis.com/maps/api/geocode/json',
     {
       key: 'AIzaSyAyz_eMufP6fT-krchIpNGbKaSJE1T1oxA',
       address: $(this).prev().text()
     },
     moveToIt
   );
}

function moveToIt(response) {
  var location = response.results[0].geometry.location;
  var latLng = new google.maps.LatLng(location.lat, location.lng);
  map.panTo(latLng);
  new google.maps.Marker({
    position: latLng,
    map: map,
    title: 'Hello World!'
  });
}
