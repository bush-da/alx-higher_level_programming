#!/usr/bin/node
const dict = require('./101-data').dict;
const myDict = {};

for (const key in dict) {
  if (myDict[dict[key]]) {
    myDict[dict[key]].push(key);
  } else {
    myDict[dict[key]] = [key];
  }
}
console.log(myDict);
