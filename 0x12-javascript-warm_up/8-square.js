#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
