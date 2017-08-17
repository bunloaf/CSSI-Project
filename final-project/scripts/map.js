var map;

function initMap() {
  var myLatLng = {lat: 33.9698, lng: -118.4185};

  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}
