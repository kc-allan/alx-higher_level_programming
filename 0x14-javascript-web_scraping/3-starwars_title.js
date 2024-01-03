#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    console.log(res.title);
  }
});
