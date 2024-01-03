#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
