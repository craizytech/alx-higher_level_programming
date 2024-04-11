#!/usr/bin/node
const arg1 = Number(process.argv[2]);
if (!isNaN(arg1)) {
  console.log('My number:', arg1);
} else {
  console.log('Not a number');
}
