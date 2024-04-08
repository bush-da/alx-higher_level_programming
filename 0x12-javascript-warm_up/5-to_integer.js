#!/usr/bin/node
const myVar = process.argv[2];
console.log(parseInt(myVar) ? 'My number: ' + parseInt(myVar) : 'Not a number');
