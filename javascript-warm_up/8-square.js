#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const numTimes = parseInt(argv[2]);
  const caracter = 'X';
  for (let i = 0; i < numTimes; i++) {
    const cadena = caracter.repeat(numTimes);
    console.log(cadena);
  }
}
