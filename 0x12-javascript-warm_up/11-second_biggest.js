#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  const number = args.map(Number);
  const sortedNumber = number.sort((a, b) => b - a);
  console.log(sortedNumber[1]);
}
