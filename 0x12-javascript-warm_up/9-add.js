#!/usr/bin/node
const args = process.argv.slice(2);
const first = Number(args[0]);
const second = Number(args[1]);
if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(first + second);
}
