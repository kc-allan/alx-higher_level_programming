#!/usr/bin/node

const { argv } = require('node:process');
const args = [];

let count = 0;
argv.forEach((val, index) => {
  if (count >= 2) {
    args[index - 2] = val;
  }
  count += 1;
});
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
