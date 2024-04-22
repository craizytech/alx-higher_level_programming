#!/usr/bin/node
exports.add = function (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return a + b;
  } else {
    return NaN;
  }
};
