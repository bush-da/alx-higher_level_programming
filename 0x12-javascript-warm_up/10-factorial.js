#!/usr/bin/node
const num = parseInt(Number(process.argv[2]));

function fac (a) {
  if (a === 1) {
    return 1;
  }
  return a * fac(a - 1);
}
if (isNaN(num)) {
  console.log('NaN');
} else {
  console.log(fac(num));
}
