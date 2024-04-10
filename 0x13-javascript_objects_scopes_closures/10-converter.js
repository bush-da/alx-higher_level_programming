#!/usr/bin/node

exports.converter = function (base) {
  return arg => arg.toString(base);
};
