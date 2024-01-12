const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, statusCode) {
  const films = data.results;
  films.forEach(element => {
    $('#list_movies').append(`<li>${element.title}</li>`);
  });
});
