#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log(0);
  process.exit(0);
}
let max = parseInt(argv[2]);
let sub = 0;
for (let i = 2; i <= len; i++) {
  const num = parseInt(argv[i]);
  if (num > max) {
    sub = max;
    max = num;
  } else if (num > sub && num !== max) {
    sub = num;
  }
}
console.log(sub);
