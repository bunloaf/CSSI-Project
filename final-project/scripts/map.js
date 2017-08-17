$(document).ready(setUp);

function setUp() {
  $('#showInMap').click(geocode);
}

function geocode() {
  $.get(
     'https://maps.googleapis.com/maps/api/geocode/json',
     {
       key: 'AIzaSyAyz_eMufP6fT-krchIpNGbKaSJE1T1oxA',
       address: $(this).prev().text()
     },
     showIt
   );
}

function showIt(response) {
  var location = response.results[0].geometry.location;
  $.get(
    'https://maps.googleapis.com/maps/api/js',
    {
      key: 'AIzaSyAyz_eMufP6fT-krchIpNGbKaSJE1T1oxA',
      callback: (() => initMap(location.lat, location.lng))
    }
  )
}

function initMap(lat, lng) {
  var myLatLng = {lat: lat, lng: lng};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}
