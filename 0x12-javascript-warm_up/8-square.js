#!/usr/bin/node
const myVar = process.argv[2];
if (!parseInt(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myVar); i++) {
    for (let j = 0; j < parseInt(myVar); j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
