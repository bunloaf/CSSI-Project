$(document).ready(setUpCalendar);

function setUpCalendar() {
  $('#date_picker').on('change', showSearchResults);
}

function showSearchResults() {
  var date = $('#date_picker').val();
  window.location.replace('/events?date=' + date);
}
