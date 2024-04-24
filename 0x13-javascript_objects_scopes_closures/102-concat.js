#!/usr/bin/node

// import necessary modules
const fs = require('fs');

// Get the filepaths from the cmd args
const [, , source1, source2, dest] = process.argv;

// Read the contents of the first file
fs.readFile(source1, 'utf8', (err, data1) => {
  if (err) {
    process.exit(1);
  }
  // read contents of 2nd souce file
  fs.readFile(source2, 'utf8', (err, data2) => {
    if (err) {
      process.exit(1);
    }
    // concatenate the files contents
    const concat = data1 + data2;

    // Write the concat to the dest
    fs.writeFile(dest, concat, 'utf8', () => {});
  });
});
