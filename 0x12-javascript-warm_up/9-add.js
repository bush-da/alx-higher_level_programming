#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const num1 = parseInt(Number(process.argv[2]));
const num2 = parseInt(Number(process.argv[3]));
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
