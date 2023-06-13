#!/usr/bin/node
const args = process.argv.slice(2);
const x = 'C is fun';
if (args[0]) {
  for (let i = 0; i < args[0]; i++) {
    console.log(x);
  }
} else {
  console.log('Missing number of occurrences');
}
