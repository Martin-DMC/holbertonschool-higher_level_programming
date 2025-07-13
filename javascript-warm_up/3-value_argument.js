#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 2) {
  console.log('No argument');
} else {
  const argumentosDelUsuario = argv.slice(2);
  console.log(argumentosDelUsuario.join(' '));
}
