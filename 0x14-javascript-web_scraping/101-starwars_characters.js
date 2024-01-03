#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body).characters;
    const charactersArray = new Array(res.length);
    let counter = 0;

    res.forEach((character, index) => {
      request(`${character}`, function (err, response, body) {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          const char = JSON.parse(body);
          charactersArray[index] = char.name;
          if (++counter === res.length) {
            charactersArray.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
