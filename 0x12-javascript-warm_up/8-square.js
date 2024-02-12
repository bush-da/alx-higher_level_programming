#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
if (myVar) {
  for (let i = 0; i < myVar; i++) {
    let row = '';
    for (let j = 0; j < myVar; j++) row += 'X';
    console.log(row);
  }
} else {
  console.log('Missing size');
}
