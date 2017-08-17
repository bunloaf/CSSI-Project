$(document).ready(setUpCalendar);

function setUpCalendar() {
  $('#date-picker').on('change', showSearchResults);
}

function showSearchResults() {
  var date = $('#date-picker').val();
  $('#search-results').html("<p>RESULTS FOR " + date + " GO HERE</p>")
}
