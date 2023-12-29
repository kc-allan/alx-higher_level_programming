#!/usr/bin/node

const { argv, argv0, cwd } = require('node:process');
const args = [];

argv.forEach((val, index) => {
  if ((argv0 != val) && (val != `${cwd()}\\2-arguments.js`)) {
    args[index] = val;
  }
});
if (args.length == 0) {
  console.log('No argument');
} else {
    console.log("Arguments found");
};