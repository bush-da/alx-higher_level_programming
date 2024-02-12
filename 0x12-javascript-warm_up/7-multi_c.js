#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
if (myVar) {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
