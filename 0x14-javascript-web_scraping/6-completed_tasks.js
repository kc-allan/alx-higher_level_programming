#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body);
    const count = {};
    res.forEach(element => {
      if (element.completed === true) {
        if (element.userId in count) {
          count[element.userId] += 1;
        } else {
          count[element.userId] = 1;
        }
      }
    });
    console.log(count);
  }
});
