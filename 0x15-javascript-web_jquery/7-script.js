const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, statusCode) {
  if (statusCode == 'success') {
    $('#character').text(data.name);
  }
});
