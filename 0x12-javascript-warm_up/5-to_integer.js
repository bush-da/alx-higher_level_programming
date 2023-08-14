#!/usr/bin/node

console.log(process.argv[2] && !isNaN(process.argv[2]) ? 'My number: ' + parseInt(process.argv[2]) : 'Not a number');
