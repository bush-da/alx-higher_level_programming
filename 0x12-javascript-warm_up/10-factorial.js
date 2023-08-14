#!/usr/bin/node

function fac (a) {
  return a === 0 || isNaN(a) ? 1 : a * fac(a - 1);
}

console.log(fac(process.argv[2]));
