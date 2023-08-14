#!/usr/bin/node

const length = process.argv.length;
console.log(length === 2 ? 'No argument' : length === 3 ? 'Argument found' : 'Arguments found');
