#!/usr/bin/node

const { argv, argv0, cwd } = require('node:process');
const args = [];

argv.forEach((val, index) => {
  if ((argv0 != val) && (val != `${cwd()}\\3-value_argument.js`)) {
    args[index] = val;
  }
});
if (`${args}` != ``) {
    args.forEach((arg) => {
        console.log(arg);
    });
} else {
    console.log("No argument");
};