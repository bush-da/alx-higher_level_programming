#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else {
    for (const arg of args) {
	console.log(arg);
    }
}
