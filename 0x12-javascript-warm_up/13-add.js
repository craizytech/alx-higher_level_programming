#!/usr/bin/node
const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

exports.add = function (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return a + b;
  } else {
    return NaN;
  }
};
