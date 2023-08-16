#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (s) {
    super(s, s);
  }
};
