#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const myList = list.map((x, index) => { return x * index; });
console.log(myList);
