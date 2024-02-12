#!/usr/bin/node
function myfac (a) {
  return a === 0 || isNaN(a) ? 1 : a * myfac(a - 1);
}

console.log(myfac(parseInt(process.argv[2])));
