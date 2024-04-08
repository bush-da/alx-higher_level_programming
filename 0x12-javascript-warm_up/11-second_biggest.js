#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myVar = process.argv.slice(2).map(Number);
  const sortedArray = myVar.sort((a, b) => (b - a));
  console.log(sortedArray[1]);
}
