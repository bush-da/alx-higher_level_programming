#!/usr/bin/node
let i = 2;
const myarray = [];
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(0);
} else {
  while (!isNaN(process.argv[i])) {
    myarray.push(process.argv[i]);
    i++;
  }
  console.log(myarray.sort()[myarray.length - 2]);
}
