#!/usr/bin/node
const le = process.argv.length;
console.log(le === 2 ? 'No argument' : le === 3 ? 'Argument found' : 'Arguments found');
