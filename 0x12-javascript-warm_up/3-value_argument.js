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
if (`${args}` === `${[]}`) {
	console.log('No argument');
} else {
	args.forEach(element => {
		console.log(element);
	});
}
