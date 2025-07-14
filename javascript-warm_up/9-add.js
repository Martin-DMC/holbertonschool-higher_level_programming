#!/usr/bin/node
const { argv } = require('node:process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  const result = a + b;
  return (result);
}
console.log(add(a, b));
