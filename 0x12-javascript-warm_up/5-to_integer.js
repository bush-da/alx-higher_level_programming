#!/usr/bin/node
console.log(typeof Number(process.argv[2]) === 'number' ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
