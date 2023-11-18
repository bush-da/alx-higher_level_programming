#!/usr/bin/node
module.exports.callMeMoby = function (a, b) {
  for (let i = 0; i < a; i++) {
    b();
  }
};
