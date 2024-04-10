#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (value) {
    if (value === searchElement) {
      count += 1;
    }
  });
  return count;
};
