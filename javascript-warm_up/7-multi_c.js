#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const numTimes = parseInt(argv[2]);
  for (let i = 0; i < numTimes; i++) {
    console.log('C is fun');
  }
}
