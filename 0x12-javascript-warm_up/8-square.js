#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = size; i > 0; i--) {
    let row = '';
    for (let k = size; k > 0; k--) {
      row = row.concat('X');
    }
    console.log(row);
  }
}
