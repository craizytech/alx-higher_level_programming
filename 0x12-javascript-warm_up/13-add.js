#!/usr/bin/node
const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

exports.add = function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const result = a + b;
    console.log(result);
  } else {
    console.log('NaN');
  }
}
add(arg1, arg2);
