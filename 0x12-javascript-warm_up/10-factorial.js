#!/usr/bin/node
const args = process.argv.slice(2);
const num = args[0];
function rec (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return (num * rec(num - 1));
}
console.log(rec(num));
