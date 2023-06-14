#!/usr/bin/node
const args = process.argv.slice(2);
let num;
if (isNaN(args[0]) || isNaN(args[1])) {
  console.log(0);
} else {
  num = args[0];
  for (let i = 1; i < args.length; i++) {
    if (args[i] > num) {
      num = args[i];
    }
  }
  const index = args.indexOf(num);
  args.splice(index, 1);
  num = args[0];
  for (let i = 1; i < args.length; i++) {
    if (args[i] > num) {
      num = args[i];
    }
  }
  console.log(num);
}
