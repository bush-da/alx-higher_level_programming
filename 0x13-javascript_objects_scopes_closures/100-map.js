#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const myList = list.map((num) => num * list.indexOf(num));
console.log(myList);
