#!/usr/bin/node
if (process.argv.length !== 3) {
  console.log('Provide a file path');
} else {
  const filePath = process.argv[2];
  const fs = require('fs');
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
