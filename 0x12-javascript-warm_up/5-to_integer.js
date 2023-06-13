#!/usr/bin/node
const args = process.argv.slice(2);
const x = Number(args[0]);
if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log(x);
}
