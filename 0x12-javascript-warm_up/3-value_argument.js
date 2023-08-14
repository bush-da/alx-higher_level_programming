#!/usr/bin/node

const length = process.argv.length;
console.log(length === 2 ? 'No argument' : process.argv[2]);
