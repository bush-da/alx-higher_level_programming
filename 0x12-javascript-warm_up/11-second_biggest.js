#!/usr/bin/node

const myargs = process.argv;
if (myargs.length > 3) {
  const args = myargs.map(Number)
    .slice(2, myargs.length)
    .sort();
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
