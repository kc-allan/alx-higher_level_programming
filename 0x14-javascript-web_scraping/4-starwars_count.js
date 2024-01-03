#!/usr/bin/node
const request = require('request');
// const url = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/';
const charID = '18';

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const result = JSON.parse(body).results;
    const res = result[0].characters;
    res.forEach(element => {
      if (element.includes(charID)) {
        request(`${element}`, function (err, response, body) {
          if (err) {
            console.log(err);
          } else if (response.statusCode === 200) {
            const films = JSON.parse(body).films;
            const count = films.length;
            console.log(count);
          }
        });
      }
    });
  }
});
