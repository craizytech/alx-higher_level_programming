#!/usr/bin/node
const arg1 = Number(process.argv[2]);

function factorial (a) {
  if (a === 0 || a === 1 || a === NaN) {
    return 1;
  } else if (!isNaN(a) && a > 0) {
    return a * factorial(a - 1);
  } else {
    console.log('1');
  }
}
console.log(factorial(arg1));
