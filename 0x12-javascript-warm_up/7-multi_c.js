#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing nummber of occurrences');
}
