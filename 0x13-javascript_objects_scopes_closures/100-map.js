#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const my_list = list.map((x, index) => {return x * index});
console.log(my_list);
