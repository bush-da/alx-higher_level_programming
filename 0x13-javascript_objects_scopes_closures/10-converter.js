#!/usr/bin/node
module.exports.converter = function (base) {
  return num => num.toString(base);
};
