#!/usr/bin/node

const fac = (a) => {
  if (a === 1) {
    return 1;
  }
  return (a * fac(a - 1));
};
if (!process.argv[2]) {
  console.log(1);
} else {
  console.log(fac(parseInt(process.argv[2])));
}
