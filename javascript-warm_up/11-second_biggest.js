#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
const array = [];

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log(0);
  process.exit(0);
}
let max = argv[2];
for (let i = 2; i <= len; i++) {
  const num = parseInt(argv[i]);
  array.push(num);
  if (num > max) {
    max = num;
  }
}
let retorno = array[0];
for (let i = 0; i < array.length; i++) {
  if (retorno < array[i] && array[i] !== max) {
    retorno = array[i];
  }
}
console.log(retorno);
