#!/usr/bin/node
let i = 2;
const myarray = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  while (!isNaN(process.argv[i])) {
    myarray.push(process.argv[i]);
    i++;
  }
  console.log(myarray.sort((a, b) => a - b)[myarray.length - 2]);
}
console.log(myarray);
