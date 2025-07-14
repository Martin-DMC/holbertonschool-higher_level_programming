#!/usr/bin/node
const { argv } = require('node:process');

function factorial (num) {
  let result = 1;
  if (num === 1 || num === 0) {
    return (result);
  }
  result = num * factorial(num - 1);
  return result;
}

const num = parseInt(argv[2]);
console.log(factorial(num));
