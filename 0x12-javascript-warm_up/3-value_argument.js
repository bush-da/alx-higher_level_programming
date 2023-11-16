#!/usr/bin/node
const args = process.argv[2];
if (args.length === 0) {
  console.log('No argument');
} else {
  console.log(args);
}
