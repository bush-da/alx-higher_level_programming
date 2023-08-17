#!/usr/bin/node

exports.esrever = function (list) {
  const temp = [];
  for (let i = list.length - 1; i >= 0; i--) {
    temp.push(list[i]);
  }
  return temp;
};
