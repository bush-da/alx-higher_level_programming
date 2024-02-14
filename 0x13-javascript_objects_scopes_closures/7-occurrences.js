#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  list.forEach((element) => { if (element === searchElement) { x += 1; } });
  return x;
};
